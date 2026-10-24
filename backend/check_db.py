import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.config import settings
from app.db.neo4j_client import neo4j_client
from motor.motor_asyncio import AsyncIOMotorClient

async def check_db():
    try:
        client = AsyncIOMotorClient(settings.mongodb_url)
        db = client[settings.mongodb_db]
        entities = await db.entities.count_documents({})
        relationships = await db.relationships.count_documents({})
        print(f'Mongo Entities: {entities}, Relationships: {relationships}')
        client.close()
    except Exception as e:
        print(f'MongoDB check error: {e}')
    
    try:
        neo4j_client.connect()
        driver = neo4j_client.get_driver()
        with driver.session() as session:
            res = session.run('MATCH (n) RETURN count(n) as c')
            print(f'Neo4j Nodes: {res.single()[0]}')
            res2 = session.run('MATCH ()-[r]->() RETURN count(r) as c')
            print(f'Neo4j Edges: {res2.single()[0]}')
        neo4j_client.close()
    except Exception as e:
        print(f'Neo4j check error: {e}')

asyncio.run(check_db())
