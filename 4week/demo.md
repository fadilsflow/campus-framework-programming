# 🎯 Demo Frontend Flask SQLAlchemy CRUD

## Screenshot Frontend

Frontend ini memiliki fitur-fitur berikut:

### 1. **Interface yang Menarik**

- Design modern dengan gradient colors
- Responsive design untuk mobile dan desktop
- Animasi hover effects
- Loading states dan error handling

### 2. **Fitur CRUD Lengkap**

#### ➕ **Create User**

- Form untuk input name dan email
- Validasi input real-time
- Feedback sukses/error

#### 👁️ **Read Users**

- Menampilkan semua users dalam card format
- Menampilkan ID, name, email, dan created_at
- Auto-refresh setelah operasi

#### ✏️ **Update User**

- Klik tombol "Edit" pada user card
- Form akan terisi dengan data user yang dipilih
- Tombol "Update User" untuk menyimpan perubahan
- Tombol "Cancel" untuk membatalkan edit

#### 🗑️ **Delete User**

- Klik tombol "Delete" pada user card
- Konfirmasi sebelum menghapus
- Auto-refresh setelah penghapusan

### 3. **Fitur Tambahan**

- **Real-time Feedback**: Pesan sukses/error muncul otomatis
- **Form Validation**: Validasi email dan required fields
- **Duplicate Prevention**: Mencegah email duplikat
- **Responsive Design**: Tampil baik di semua ukuran layar

## Cara Menggunakan

1. **Jalankan aplikasi:**

   ```bash
   python run.py
   # atau
   python main.py
   ```

2. **Buka browser:**

   ```
   http://localhost:5000
   ```

3. **Test CRUD operations:**
   - Buat user baru dengan mengisi form
   - Lihat user yang sudah dibuat
   - Edit user dengan klik tombol "Edit"
   - Hapus user dengan klik tombol "Delete"

## Teknologi yang Digunakan

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Flask, SQLAlchemy, MySQL
- **Styling**: Custom CSS dengan gradient dan animations
- **API**: RESTful API dengan JSON responses

## Struktur File

```
4week/
├── main.py              # Flask aplikasi utama
├── templates/
│   └── index.html       # Frontend interface
├── requirements.txt     # Python dependencies
├── test_api.py         # Script testing API
├── run.py              # Script untuk menjalankan app
├── README.md           # Dokumentasi
└── demo.md            # File ini
```

## API Endpoints yang Digunakan Frontend

- `GET /` - Melayani halaman frontend
- `GET /users` - Mengambil semua users
- `POST /users` - Membuat user baru
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Hapus user

Frontend ini memberikan pengalaman yang smooth dan intuitif untuk testing semua operasi CRUD dengan database MySQL melalui Flask SQLAlchemy!
