from app.crud import (
    criar_departamento,
    listar_departamentos,
    atualizar_departamento,
    desativar_departamento
)

from app.database import SessionLocal


db = SessionLocal()

try:
    # Criar
    novo = criar_departamento(db, 'Jurídico', 'JUR')
    print(f"Criado: {novo.nome} ({novo.sigla})")

    # Listar
    todos = listar_departamentos(db)
    print(f"Total: {len(todos)} departamentos")

    # Atualizar
    atualizado = atualizar_departamento(
        db,
        novo.id,
        'Jurídico e Compliance'
    )
    print(f"Atualizado: {atualizado.nome}")

    # Desativar
    desativado = desativar_departamento(db, novo.id)
    print(f"Desativado: {desativado.nome} - ativo={desativado.ativo}")

finally:
    db.close()