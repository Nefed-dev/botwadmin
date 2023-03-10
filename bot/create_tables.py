from base import Base, engine, Session


def create_tables():
    print("Drop existing tables")
    # Base.metadata.drop_all(engine)
    # Session.commit()
    print("Run create tables")
    Base.metadata.create_all(engine)
    Session.commit()
    print("Create tables - OK")


def main():
    create_tables()


if __name__ == "__main__":
    main()
