import asyncio, os, json, sys
sys.path.append('d:/crimenet/backend')
from dotenv import load_dotenv
load_dotenv('d:/crimenet/backend/.env')
from app.pipelines.sources.fir_pipeline import FIRPipeline

async def t():
    p = FIRPipeline('t')
    text = await p.extract('d:/crimenet/demo_fir_3.txt')
    clean = await p.process(text)
    ent = await p.extract_entities(clean)
    print(json.dumps(ent, indent=2))

if __name__ == "__main__":
    asyncio.run(t())
