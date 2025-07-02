from neo4j import GraphDatabase
import spacy
from typing import List, Dict

class KnowledgeGraphProcessor:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.nlp = spacy.load('en_core_web_lg')

    def close(self):
        self.driver.close()

    def create_entity(self, entity_type: str, properties: Dict):
        with self.driver.session() as session:
            session.write_transaction(
                self._create_entity_tx,
                entity_type,
                properties
            )

    @staticmethod
    def _create_entity_tx(tx, entity_type: str, properties: Dict):
        query = (
            f"CREATE (n:{entity_type} $properties)"
        )
        tx.run(query, properties=properties)

    def create_relationship(self, start_node: Dict, end_node: Dict, relationship_type: str):
        with self.driver.session() as session:
            session.write_transaction(
                self._create_relationship_tx,
                start_node,
                end_node,
                relationship_type
            )

    @staticmethod
    def _create_relationship_tx(tx, start_node: Dict, end_node: Dict, relationship_type: str):
        query = (
            f"MATCH (a:{start_node['type']}), (b:{end_node['type']}) "
            f"WHERE a.id = $start_id AND b.id = $end_id "
            f"CREATE (a)-[r:{relationship_type}]->(b)"
        )
        tx.run(query, start_id=start_node['id'], end_id=end_node['id'])