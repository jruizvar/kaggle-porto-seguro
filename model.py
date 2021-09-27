from imblearn.over_sampling import SMOTE
from imblearn.pipeline import make_pipeline as imb_make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.impute import MissingIndicator, SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
import os
import pandas as pd


class Model:
    """ Class to create a model.

        Parameters
        ----------
        n_features: int
            Número de variáveis a serem exploradas.

        n_bins: int
            Número de bins na discretização de variáveis.
    """
    def __init__(self, n_features, n_bins):
        self.n_features = n_features
        self.n_bins = n_bins
        self._columns = ['var1']
        self._score = 0.
        self._estimator = None

    def _model(self):
        """ Método para definir o pipeline com as etapas
            de dataprep, over sampling, e algoritmo.

            Return
            ------
            _pipeline: function
        """
        def _pipeline(columns):
            dataprep = make_pipeline(
                SimpleImputer(strategy='median'),
                KBinsDiscretizer(n_bins=self.n_bins, strategy='uniform'),
            )
            transformer = make_column_transformer(
                (MissingIndicator(), columns),
                (dataprep, columns),
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
        return _pipeline

    def _evaluate(self, X, y, columns):
        """ Avalia o modelo usando as colunas selecionadas
            e retorna o F1-score.

            Parameters
            ----------
            X: pd.DataFrame
            y: pd.Series
            columns: List[str]

            Return
            ------
            score: float
        """
        pipeline = self._model()
        clf = pipeline(columns)
        scores = cross_val_score(clf, X, y, scoring='f1', cv=15)
        score = np.mean(scores)
        return score

    def _iteratecolumns(self, X, y, n=2):
        """ Método recursivo para encontrar as melhores colunas.

            Parameters
            ----------
            X: pd.DataFrame
            y: pd.Series
            n: int
        """
        print(f'F1-score na iteração {n-1}: {self._score:.5f}')
        if n > self.n_features:
            return self._columns
        else:
            testcols = self._columns + [f'var{n}']
            testscore = self._evaluate(X, y, testcols)
            if testscore > self._score:
                self._columns = testcols
                self._score = testscore
            return self._iteratecolumns(X, y, n+1)

    def train(self, X, y):
        """ Método para treinar o modelo.

            Parameters
            ----------
            X: pd.DataFrame
            y: pd.Series
        """
        cols = self._iteratecolumns(X, y)
        pipeline = self._model()
        clf = pipeline(cols)
        clf.fit(X, y)
        self._estimator = clf

    def submit(self, X_test, outfile, upload=False):
        """ Método para criar arquivo de submissão
            conforme a formatação do Kaggle.

            Parameters
            ----------
            X_test: pd.DataFrame
            outfile: str
            upload: bool
        """
        clf = self._estimator
        y_pred = clf.predict(X_test)
        s = pd.Series(y_pred, index=X_test.index, name='predicted')
        s.to_csv(outfile)
        if upload:
            submit_to_kaggle = (
                f"kaggle competitions submit -f {outfile} "
                "-m 'Submissão do dia' porto-seguro-data-challenge"
            )
            os.system(submit_to_kaggle)
