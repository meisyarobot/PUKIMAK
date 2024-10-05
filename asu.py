from pymongo import MongoClient

# URL koneksi MongoDB
mongo_url = "mongodb+srv://arkanasamudra33:arkana21@cluster0.4swy3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Membuat koneksi ke MongoDB
client = MongoClient(mongo_url)

# Memilih database (ganti dengan nama database kamu)
db = client['your_database']

# Memilih koleksi (ganti dengan nama koleksi kamu)
collection = db['your_collection']

# Mengambil semua dokumen dari koleksi
documents = collection.find()

# Menampilkan hanya string yang terkait dengan pengguna Telegram
for doc in documents:
    # Misalkan data user Telegram ada di dalam field username, first_name, last_name
    user_info = {}
    if 'username' in doc and isinstance(doc['username'], str):
        user_info['username'] = doc['username']
    if 'first_name' in doc and isinstance(doc['first_name'], str):
        user_info['first_name'] = doc['first_name']
    if 'last_name' in doc and isinstance(doc['last_name'], str):
        user_info['last_name'] = doc['last_name']
    
    # Tampilkan info user jika ada data string terkait
    if user_info:
        print(user_info)
