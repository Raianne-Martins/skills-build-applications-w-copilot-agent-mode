from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Listar coleções
collections = db.list_collection_names()
if not collections:
    print("Nenhuma coleção encontrada no banco de dados.")
else:
    print("Coleções encontradas:", collections)

# Verificar se cada coleção contém documentos
for collection_name in collections:
    collection = db[collection_name]
    count = collection.count_documents({})
    print(f"\nColeção {collection_name} contém {count} documentos.")
    if count > 0:
        for document in collection.find():
            print(document)
