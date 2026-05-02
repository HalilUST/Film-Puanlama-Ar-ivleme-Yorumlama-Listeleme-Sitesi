from flask import Blueprint, render_template, request, redirect, url_for, session

views = Blueprint('views', __name__)

# 1. ANA SAYFA KONTROLÜ
@views.route('/')
def home():
    # Eğer kullanıcının bilekliği varsa direkt içeri (dashboard) al
    if 'kullanici' in session:
        return redirect(url_for('views.dashboard'))
    # Bilekliği yoksa kapıya (login) yönlendir
    return redirect(url_for('views.login'))

# 2. GİRİŞ YAP SAYFASI
@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        kullanici_adi = request.form.get('username')
        sifre = request.form.get('password')
        
        # İleride burada Burak'ın veritabanına "Bu şifre doğru mu?" diye soracağız.
        # Şimdilik herkesi doğru kabul edip bilekliği takıyoruz:
        session['kullanici'] = kullanici_adi
        
        # Giriş başarılı, onu direkt içerideki sayfaya fırlat:
        return redirect(url_for('views.dashboard'))
    
    return render_template("login.html")

# 3. YENİ: İÇERİDEKİ ÖZEL SAYFA (DASHBOARD)
@views.route('/dashboard')
def dashboard():
    # Güvenlik Kontrolü: Bu adamın bilekliği var mı?
    if 'kullanici' in session:
        aktif_isim = session['kullanici']
        return f"<h1>Hosgeldin {aktif_isim}! Burasi sadece giris yapanlarin gordugu ozel sayfa. <br><br> <a href='/logout'>Cikis Yap</a></h1>"
    else:
        # Bilekliği yoksa (linki ezberleyip kaçak girmeye çalışıyorsa) login'e kışla
        return redirect(url_for('views.login'))

# 4. YENİ: ÇIKIŞ YAPMA (LOGOUT)
@views.route('/logout')
def logout():
    # session.pop ile bilekliği çöpe atıyoruz
    session.pop('kullanici', None)
    return redirect(url_for('views.login'))

# 5. KAYIT OL SAYFASI (Eski haliyle kalabilir)
@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        kullanici_adi = request.form.get('username')
        sifre = request.form.get('password')
        return f"<h1>KAYIT BASARILI -> Kullanici: {kullanici_adi}, Sifre: {sifre}</h1>"
    return render_template("register.html")

@views.route('/film/<int:id>')
def film_detay(id):
    return f"<h1>Burasi {id} numarali filmin sayfasi. Detaylar gelecek.</h1>"