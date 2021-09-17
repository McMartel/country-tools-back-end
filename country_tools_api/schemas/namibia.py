import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy.orm import scoped_session, sessionmaker

from database.base import db_session
from database import namibia as namibia_db

from .util import sqlalchemy_filter

# HS Classification
class NamibiaHSClassification(SQLAlchemyObjectType):
    class Meta:
        model = namibia_db.NamibiaHSClassification
        interfaces = (graphene.relay.Node,)


# NAICS Classification
class NamibiaNAICSClassification(SQLAlchemyObjectType):
    class Meta:
        model = namibia_db.NamibiaNAICSClassification
        interfaces = (graphene.relay.Node,)


# HS Factors
class NamibiaHSFactors(SQLAlchemyObjectType):
    class Meta:
        model = namibia_db.NamibiaHSFactors
        interfaces = (graphene.relay.Node,)


# NAICS Factors
class NamibiaNAICSFactors(SQLAlchemyObjectType):
    class Meta:
        model = namibia_db.NamibiaNAICSFactors
        interfaces = (graphene.relay.Node,)


class NamibiaQuery(graphene.ObjectType):
    namibia_hs_list = graphene.List(NamibiaHSClassification)
    namibia_hs = graphene.Field(
        NamibiaHSClassification, hs_id=graphene.Int(required=True)
    )

    namibia_naics_list = graphene.List(NamibiaNAICSClassification)
    namibia_naics = graphene.Field(
        NamibiaNAICSClassification, naics_id=graphene.Int(required=True)
    )

    def resolve_namibia_hs_list(self, info, **args):
        return db_session.query(namibia_db.NamibiaHSClassification)

    def resolve_namibia_hs(self, info, **args):
        return (
            db_session.query(namibia_db.NamibiaHSClassification)
            .filter(
                getattr(namibia_db.NamibiaHSClassification, "hs_id") == args["hs_id"]
            )
            .one()
        )

    def resolve_namibia_naics_list(self, info, **args):
        return db_session.query(namibia_db.NamibiaNAICSClassification)

    def resolve_namibia_naics(self, info, **args):
        return (
            db_session.query(namibia_db.NamibiaNAICSClassification)
            .filter(
                getattr(namibia_db.NamibiaNAICSClassification, "naics_id")
                == args["naics_id"]
            )
            .one()
        )
