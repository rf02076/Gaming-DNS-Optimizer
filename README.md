# 🎮 Gaming DNS Optimizer

A powerful Windows GUI application built with Python and CustomTkinter, designed to help gamers find, test, and apply the best DNS servers to reduce ping, eliminate packet loss, and bypass network restrictions.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

---

## ✨ Features (English)

- **⚡ DNS Latency Test:** Tests multiple Iranian and foreign DNS servers (Shecan, Radar, Electro, Cloudflare, etc.) to find the lowest ping and jitter.
- **🌐 DNS Speed Test:** Measures actual download speed through different DNS servers.
- **🎯 Profiles:** Create one-click profiles for your favorite games.
- **📊 Detailed Analysis:** Shows Jitter, Packet Loss, P95/P99 latency, and Bufferbloat.
- **🛠 Manual Target Ping:** Ping custom game servers directly (e.g., LoL EU, Valorant).
- **⚙ Settings:** Fully customizable DNS list and UI themes.

> [!IMPORTANT]  
> **This application MUST be run as Administrator.**  
> Applying DNS settings requires modifying Windows network adapter configurations, which is not possible without elevated privileges. If you don't run it as Admin, you will see "Error! Run as Admin" messages.

## 🚀 Installation (For Users)

1. Go to the [Releases](https://github.com/YOUR_USERNAME/YOUR_REPO/releases) page.
2. Download the latest `DNS Optimizer.exe` or the Installer.
3. **Right-click the file and select "Run as Administrator".**
4. Enjoy lower ping!

## 💻 Build from Source (For Developers)

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

2.Install dependencies:

    pip install -r requirements.txt

3.Run the app:
    python main.py



📦 How to Convert to .EXE (Using PyInstaller)
You can easily convert this Python script into a standalone Windows executable using pyinstaller.

1.Install PyInstaller:
    pip install pyinstaller

2.Run the following command in the project directory:
    pyinstaller --noconfirm --onefile --windowed --icon=PD.ico --name="DNS Optimizer" main.py
    (Note: The --windowed flag prevents the black CMD console from appearing behind the GUI).

3.Your .exe file will be ready in the dist/ folder.


🤝 Contributing
Contributions are welcome! If you have a DNS server to add or a feature to suggest, please open an Issue or a Pull Request.

📝 License
This project is licensed under the MIT License.


🎮 بهینه‌ساز DNS گیمینگ (فارسی)
یک برنامه گرافیکی قدرتمند برای ویندوز که با پایتون و CustomTkinter ساخته شده است. این ابزار به گیمرها کمک می‌کند تا بهترین سرورهای DNS را پیدا، تست و اعمال کنند تا پینگ (Ping) را کاهش دهند، افت بسته (Packet Loss) را از بین ببرند و محدودیت‌های شبکه را دور بزنند.

✨ امکانات (فارسی)
⚡ تست تاخیر DNS: تست چندین DNS ایرانی و خارجی (شکن، رادار، الکترو، کلودفلر و...) برای پیدا کردن کمترین پینگ و جیتر.

🌐 تست سرعت DNS: اندازه‌گیری سرعت دانلود واقعی از طریق DNSهای مختلف.

🎯 پروفایل‌ها: ساخت پروفایل‌های یک کلیکی برای بازی‌های مورد علاقه‌تان.

📊 تحلیل دقیق: نمایش جیتر (Jitter)، افت بسته (Packet Loss)، پینگ P95/P99 و بافر‌بلوت (Bufferbloat).

🛠 پینگ دستی: پینگ مستقیم سرورهای بازی (مثل LoL EU یا Valorant).

⚙ تنظیمات: لیست DNS کاملاً قابل شخصی‌سازی و تم‌های رابط کاربری.

[!IMPORTANT]
این برنامه حتماً باید با دسترسی Administrator (ادمین) اجرا شود.
اعمال تنظیمات DNS نیاز به تغییر در تنظیمات شبکه ویندوز دارد که بدون دسترسی ادمین امکان‌پذیر نیست. اگر برنامه را با ادمین اجرا نکنید، با پیام "Error! Run as Admin" مواجه خواهید شد.

🚀 نصب و راه‌اندازی (برای کاربران)
به صفحه Releases بروید.

آخرین نسخه DNS Optimizer.exe یا فایل نصب‌کننده را دانلود کنید.

روی فایل راست‌کلیک کنید و گزینه "Run as Administrator" (اجرا به عنوان مدیر) را انتخاب کنید.

از پینگ پایین‌تر لذت ببرید!

💻 ساخت از روی سورس کد (برای توسعه‌دهندگان)

🤝 مشارکت
از مشارکت شما استقبال می‌کنیم! اگر DNS سروری برای اضافه کردن دارید یا پیشنهادی برای ویژگی‌ها دارید، لطفاً یک Issue یا Pull Request باز کنید.