
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Player, Quiz, Question



if __name__=='__main__':
    engine = create_engine ('sqlite:///studying-VScode-shortcut-quiz.db')
    Base.metada.create.all(engine)
    Session=sessionmaker (bind=engine)
    session=Session()

    
    import ipdb; ipdb.set_trace()