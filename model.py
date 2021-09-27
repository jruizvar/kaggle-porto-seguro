from imblearn.over_sampling import SMOTE
from imblearn.pipeline import make_pipeline as imb_make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.impute import MissingIndicator, SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import KBinsDiscretizer, MaxAbsScaler
import numpy as np
import os
import pandas as pd


class Model:
    """ Class to create a model.

        Parameters
        ----------
        version: int
            Supported versions are 1 or 2

        n_bins: int
            Controls de discretization granularity
    """
    def __init__(self, version, n_bins):
        self.version = version
        self.n_bins = n_bins
        self.cols_ = ['var1']
        self.score_ = 0.3
        self.estimator_ = None

    def dataprep(self):
        """ Define diferentes pipelines de preparação dos dados
            segundo o número de versão.
        """
        if self.version == 1:
            return make_pipeline(
                SimpleImputer(strategy='median'),
                MaxAbsScaler(),
            )
        elif self.version == 2:
            return make_pipeline(
                SimpleImputer(strategy='median'),
                KBinsDiscretizer(n_bins=self.n_bins, strategy='uniform'),
            )
        else:
            return 'drop'

    def model(self):
        """ Método para definir o pipeline com as etapas
            de dataprep, over sampling, e algoritmo.

            Return
            ------
            pipeline: function
        """
        def pipeline(cols):
            transformer = make_column_transformer(
                (MissingIndicator(), cols),
                (self.dataprep(), cols),
            )
            kargs = {
                'C': 0.1,
                'solver': 'liblinear',
                'random_state': 42,
            }
            return imb_make_pipeline(
                transformer,
                SMOTE(random_state=42),
                LogisticRegression(**kargs),
            )
        return pipeline

    def evaluate(self, X, y, cols):
        """ Executa o modelo na lista cols e retorna o score.

            Return
            ------
            score: float
        """
        pipeline = self.model()
        clf = pipeline(cols)
        scores = cross_val_score(clf, X, y, scoring='f1', cv=15)
        score = np.mean(scores)
        return score

    def iteratecolumns(self, X, y, ncol=2):
        """ Método recursivo para encontrar as melhores colunas.
        """
        print(f'score at iteration {ncol-1}: {self.score_:.5f}')
        max_iterations = 20
        if ncol > max_iterations:
            return self.cols_
        else:
            testcol = f'var{ncol}'
            testcols = self.cols_ + [testcol]
            testscore = self.evaluate(X, y, testcols)
            if testscore > self.score_:
                self.cols_ = testcols
                self.score_ = testscore
            return self.iteratecolumns(X, y, ncol+1)

    def train(self, X, y):
        """ Método para treinar o modelo.

            Parameters
            ----------
            X: pd.DataFrame
            y: pd.Series
        """
        cols = self.iteratecolumns(X, y)
        pipeline = self.model()
        clf = pipeline(cols)
        clf.fit(X, y)
        self.estimator_ = clf

    def submit(self, X_test, outfile, upload=False):
        """ Método para criar arquivo de submissão
            conforme a sintaxe do Kaggle.

            Parameters
            ----------
            X_test: pd.DataFrame
            outfile: str
            upload: bool
        """
        clf = self.estimator_
        y_pred = clf.predict(X_test)
        s = pd.Series(y_pred, index=X_test.index, name='predicted')
        s.to_csv(outfile)
        if upload:
            submit_to_kaggle = (
                f"kaggle competitions submit -f {outfile} "
                "-m 'Submissão do dia' porto-seguro-data-challenge"
            )
            os.system(submit_to_kaggle)
