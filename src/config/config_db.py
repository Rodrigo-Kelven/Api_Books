from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


Base = declarative_base()

# Use aiosqlite para SQLite
DATABASE_URL = "sqlite+aiosqlite:///./Banco_de_Dados/books_db.db"

# Criação do engine assíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Criação da sessão assíncrona
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Função para obter a sessão do banco de dados
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session