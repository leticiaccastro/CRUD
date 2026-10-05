
from sqlalchemy.orm import Session
from .models import Departamento


def criar_departamento(db: Session, nome: str, sigla: str):
    # Verificar se a sigla já existe
    existe = db.query(Departamento).filter(
        Departamento.sigla == sigla
    ).first()

    if existe:
        raise ValueError(f"Sigla {sigla} já cadastrada")

    novo = Departamento(nome=nome, sigla=sigla)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_departamentos(db: Session):
    return db.query(Departamento).order_by(
        Departamento.nome
    ).all()


def buscar_depto_por_id(db: Session, depto_id: int):
    return db.query(Departamento).filter(
        Departamento.id == depto_id
    ).first()


def atualizar_departamento(db: Session, depto_id: int, nome: str):
    depto = buscar_depto_por_id(db, depto_id)

    if not depto:
        raise ValueError(f"Departamento {depto_id} não encontrado")

    depto.nome = nome
    db.commit()
    db.refresh(depto)
    return depto


def desativar_departamento(db: Session, depto_id: int):
    depto = buscar_depto_por_id(db, depto_id)

    if not depto:
        raise ValueError(f"Departamento {depto_id} não encontrado")

    depto.ativo = False
    db.commit()
    return depto