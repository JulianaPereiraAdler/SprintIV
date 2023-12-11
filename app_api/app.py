from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Model
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="API (MVP - Sprint 4)", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
doc_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")


@app.get('/swagger', tags=[doc_tag])
def swagger():
    """Redireciona para a documentação Swagger."""
    return redirect('/openapi/swagger')


@app.get('/documentacao', tags=[doc_tag])
def documentacao():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag], responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.
    
    Args:
        nome (str): nome do paciente
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    session = Session()
    
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        return apresenta_pacientes(pacientes), 200



# Rota de adição de paciente
@app.post('/paciente_predict', tags=[paciente_tag], responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def paciente_predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
        name (str) : nome do paciente
        age (int): idade do paciente em anos.
        sex (int): sexo do paciente [Masculino = 1, Feminino=0]
        chest_pain_type (int): tipo de Dor no Peito inclui Angina Típica (TA = 3), Angina Atípica (ATA = 1), Dor Não Anginal (NAP = 2) e Assintomático (ASY = 0)
        resting_B (int): pressão Arterial em Repouso: Medida em mm Hg
        cholesterol (int): colesterol, medido em mm/dl.
        fasting_BS (int): glicemia em jejum, indica diabetes se > 120 mg/dl.
        resting_ECG (int): ECG em Repouso, inclui normal (1), anormalidades de onda ST-T (2), e hipertrofia ventricular esquerda (0).
        max_HR (int): Frequência Cardíaca Máxima: Valor numérico entre 60 e 202.
        exercise_Angina (int): Angina Induzida por Exercício, indica a presença ou ausência de angina.
        oldpeak (float): Depressão de ST induzida por exercício em relação ao repouso, medida em milímetros.
        st_Slope (int): classificado como ascendente (2), plano (1) ou descendente (2).
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    print("------------------------------------------------------------------------------")
    print(form)
    # Carregando modelo
    ml_path = 'ml_model/model.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    paciente = Paciente(
        name = form.name.strip(),
        age = form.age,
        sex= form.sex,
        chest_pain_type = form.chest_pain_type,
        resting_BP = form.resting_BP,
        cholesterol = form.cholesterol,
        fasting_BS = form.fasting_BS,
        resting_ECG = form.resting_ECG,
        max_HR = form.max_HR,
        exercise_Angina = form.exercise_Angina,
        oldpeak = form.oldpeak,
        st_Slope = form.st_Slope, 
        outcome=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando produto de nome: '{paciente.name}'")
    
    try:
        session = Session()
        
        if session.query(Paciente).filter(Paciente.name == form.name).first():
            error_msg = "Paciente já existente na base :/"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        session.add(paciente)
        session.commit()
        logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400


# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag], responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{paciente_nome}")
    session = Session()
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = f"Paciente {paciente_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag], responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    session = Session()
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso!"}, 200