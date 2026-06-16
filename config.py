class Config:
    SECRET_KEY = "troque-esta-chave-em-producao"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:senha@localhost/sistema_login"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False