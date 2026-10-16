# 🎮 Gaming DNS Optimizer

**A lightweight Windows application for testing, comparing, and managing DNS servers for gaming and everyday use.**

Gaming DNS Optimizer is a desktop application built with **Python and CustomTkinter** that helps users test different DNS servers and choose a suitable configuration based on their own network performance.

Instead of assuming that one DNS server is always the best, the application allows you to measure and compare **Ping, Jitter, Packet Loss, DNS performance, and Download Speed**.

> **Created by RF020**

---

## ✨ Features

### ⚡ DNS Latency Test

Test multiple DNS servers and compare their network performance.

- Ping measurement
- Jitter calculation
- Packet Loss detection
- P95 / P99 latency
- Best / Worst response
- Stability measurement
- Performance score from 0–100
- Multiple test modes
- Parallel DNS testing
- Manual IP / Domain ping
- One-click DNS application

The latency score is calculated using Ping, Jitter, and Packet Loss rather than relying on a single ping result.

---

### 🌐 DNS Speed Test

Compare download performance through different DNS configurations.

Available test modes:

| Mode | Test Size |
|---|---:|
| ⚡ Fast | 1 MB |
| ⚖️ Medium | 3 MB |
| 🚀 Optimal | 5 MB |

You can also configure custom test links and compare speed and test duration.

---

### 📊 Analytics

Analyze and compare your previous DNS tests.

You can compare:

- Last 3 tests
- Last 5 tests
- Last 10 tests
- Last 20 tests
- Latency history
- Speed history
- Average score
- Average Ping
- Stability
- Best result
- Worst result
- Successful test count

The Analytics section is designed to make it easier to evaluate DNS performance over multiple test runs instead of relying on a single measurement.

---

### 🎯 Game Profiles

Create custom DNS profiles for your favorite games.

For example:

```text
🎮 League of Legends
├── DNS 1
└── DNS 2

🎮 Valorant
├── DNS 1
└── DNS 2

🎮 Custom Game
├── DNS 1
└── DNS 2
```

Profiles can be created, edited, stored, and applied quickly from the application.

---

### 🌍 DNS Library

Gaming DNS Optimizer includes a DNS library with categorized servers.

Categories can include:

- 🎮 Gaming
- 🌍 Foreign Gaming
- 🛡️ Security
- 🔓 Anti-Filter
- 📡 Standard

Users can manage and organize their DNS configurations locally.

---

### 📋 Activity Logs

Keep track of application activity through the built-in logging system.

Logs include:

- INFO
- SUCCESS
- WARNING
- ERROR
- DNS changes
- Test activity
- Profile actions
- Application events

Logs can be filtered and refreshed directly from the application.

---

## 🖥️ Interface

Gaming DNS Optimizer uses a modern dark interface built with **CustomTkinter**.

Main sections:

```text
⚡ DNS Latency Test
🌐 DNS Speed Test
📊 Analytics
🎯 Game Profiles
⚙️ Settings
📋 Activity Logs
```

The application also maintains local configuration, DNS profiles, and test history.

---

## 🧠 How It Works

Gaming DNS Optimizer does **not** claim that one DNS server is universally the fastest.

DNS performance can vary depending on:

- ISP
- Geographic location
- Network routing
- Server availability
- Network congestion
- Internet conditions

For this reason, the application allows you to test DNS servers directly from your own connection.

### Latency Evaluation

The latency test considers:

```text
Ping
Jitter
Packet Loss
```

These values are combined into a performance score between **0 and 100**.

A higher score represents better performance according to the application's scoring system.

---

## 🚀 Installation

### Windows

Download the latest available release from the **Releases** section of this repository.

Run the application and select the DNS configuration you want to test.

### Run From Source

Clone the repository:

```bash
git clone https://github.com/rf02076/Gaming-DNS-Optimizer.git
```

Enter the project directory:

```bash
cd Gaming-DNS-Optimizer
```

Install the required dependencies:

```bash
pip install customtkinter pillow
```

Then run the application:

```bash
python main.py
```

> The exact entry-point filename may depend on the current project structure.

---

## ⚠️ Important

Gaming DNS Optimizer is a **DNS testing and management tool**.

Changing DNS does not directly increase your Internet bandwidth or guarantee lower in-game ping.

Actual performance depends on your ISP, routing, location, DNS server availability, and the destination server.

For better results, run multiple tests at different times and compare the historical data.

---

## 🔐 Privacy

Gaming DNS Optimizer is designed around local configuration and local test history.

Application configuration, test history, and activity information are stored locally on the Windows system.

---

## 🧰 Built With

- 🐍 Python
- 🖥️ CustomTkinter
- Tkinter
- Windows `ping`
- Windows `nslookup`
- Windows `netsh`
- JSON
- Threading / ThreadPoolExecutor

Multiple DNS servers can be tested using parallel workers.

---

## 🎮 Who Is It For?

Gaming DNS Optimizer is intended for:

- PC gamers
- Users who want to compare DNS servers
- Users experiencing DNS-related connection issues
- Users who want a graphical DNS management tool
- Gamers who want to test DNS performance from their own connection
- Users who want to keep and compare historical test results

---

## 📸 Screenshots

Add application screenshots here.

Recommended screenshots:

1. DNS Latency Test
2. DNS Speed Test
3. Analytics
4. Game Profiles
5. Settings
6. Activity Logs

---

## 🗺️ Roadmap

Possible future improvements:

- [ ] Automatic DNS recommendation
- [ ] Advanced network diagnostics
- [ ] Game-specific testing
- [ ] Detailed performance charts
- [ ] Background monitoring
- [ ] Custom scoring system
- [ ] DNS library import / export
- [ ] Multi-language interface
- [ ] Improved Windows installer
- [ ] Automatic updates

---

# 🇮🇷 فارسی

## 🎮 Gaming DNS Optimizer چیست؟

**Gaming DNS Optimizer** یک برنامه ویندوزی سبک برای **تست، مقایسه و مدیریت DNS** است که با Python و CustomTkinter ساخته شده است.

هدف برنامه این است که به جای انتخاب یک DNS به صورت تصادفی یا صرفاً بر اساس پیشنهاد دیگران، بتوانید DNSهای مختلف را **از طریق اینترنت و شبکه خودتان** آزمایش و عملکرد آن‌ها را با یکدیگر مقایسه کنید.

برنامه معیارهایی مانند:

- Ping
- Jitter
- Packet Loss
- DNS Performance
- Download Speed
- Stability
- Performance Score

را بررسی می‌کند.

---

## ⚡ تست Latency

در بخش **DNS Latency Test** می‌توانید چندین DNS را بررسی کرده و نتایج آن‌ها را با یکدیگر مقایسه کنید.

موارد قابل بررسی:

- میانگین Ping
- Jitter
- Packet Loss
- P95 Latency
- P99 Latency
- بهترین و بدترین نتیجه
- میزان Stability
- امتیاز عملکرد از ۰ تا ۱۰۰

برنامه برای امتیازدهی فقط به Ping نگاه نمی‌کند و **Ping، Jitter و Packet Loss** را در نظر می‌گیرد.

---

## 🌐 تست سرعت DNS

در بخش **DNS Speed Test** می‌توانید عملکرد DNSهای مختلف را از نظر سرعت دانلود مقایسه کنید.

سه حالت تست وجود دارد:

| حالت | حجم تست |
|---|---:|
| ⚡ Fast | 1 MB |
| ⚖️ Medium | 3 MB |
| 🚀 Optimal | 5 MB |

همچنین امکان استفاده از لینک‌های تست سفارشی وجود دارد.

---

## 📊 Analytics

در بخش **Analytics** می‌توانید نتایج تست‌های قبلی را با یکدیگر مقایسه کنید.

امکانات:

- مقایسه ۳ تست اخیر
- مقایسه ۵ تست اخیر
- مقایسه ۱۰ تست اخیر
- مقایسه ۲۰ تست اخیر
- مقایسه تست‌های Latency
- مقایسه تست‌های Speed
- میانگین امتیاز
- میانگین Ping
- Stability
- بهترین نتیجه
- بدترین نتیجه
- تعداد دفعات موفقیت DNS

این قسمت کمک می‌کند انتخاب DNS فقط بر اساس یک تست انجام نشود.

---

## 🎯 Game Profiles

با استفاده از **Game Profiles** می‌توانید برای بازی‌های مختلف پروفایل اختصاصی بسازید.

مثلاً:

```text
🎮 League of Legends
├── DNS 1
└── DNS 2

🎮 Valorant
├── DNS 1
└── DNS 2
```

پروفایل‌ها ذخیره می‌شوند و می‌توانید در آینده آن‌ها را ویرایش یا سریعاً اعمال کنید.

---

## 🌍 DNS Library

برنامه دارای یک کتابخانه DNS دسته‌بندی‌شده است.

برای مثال:

- 🎮 Gaming
- 🌍 Foreign Gaming
- 🛡️ Security
- 🔓 Anti-Filter
- 📡 Standard

کاربر می‌تواند DNSهای موجود را مدیریت کرده و تنظیمات خود را در برنامه نگهداری کند.

---

## 📋 Activity Logs

در قسمت **Activity Logs** فعالیت‌های برنامه ثبت می‌شوند.

شامل:

- INFO
- SUCCESS
- WARNING
- ERROR
- تغییر DNS
- فعالیت تست‌ها
- ایجاد و ویرایش Profile
- رویدادهای برنامه

همچنین امکان فیلتر کردن و Refresh کردن لاگ‌ها وجود دارد.

---

## 🧠 برنامه چگونه کار می‌کند؟

Gaming DNS Optimizer ادعا نمی‌کند که یک DNS برای همه کاربران بهترین است.

عملکرد DNS می‌تواند با توجه به موارد زیر تغییر کند:

- ISP
- موقعیت جغرافیایی
- مسیر ارتباطی شبکه
- وضعیت سرور DNS
- شلوغی شبکه
- شرایط اینترنت

به همین دلیل، برنامه به شما اجازه می‌دهد DNSها را **مستقیماً روی اتصال اینترنت خودتان** تست کنید.

### معیارهای تست Latency

```text
Ping
Jitter
Packet Loss
```

این اطلاعات در نهایت برای محاسبه یک **Performance Score از ۰ تا ۱۰۰** استفاده می‌شوند.

---

## 🚀 نصب

### ویندوز

آخرین نسخه برنامه را از بخش **Releases** همین Repository دریافت کنید.

سپس برنامه را اجرا کرده و DNS موردنظر خود را تست یا اعمال کنید.

### اجرای سورس کد

Repository را Clone کنید:

```bash
git clone https://github.com/rf02076/Gaming-DNS-Optimizer.git
```

و وارد پوشه پروژه شوید:

```bash
cd Gaming-DNS-Optimizer
```

کتابخانه‌های موردنیاز را نصب کنید:

```bash
pip install customtkinter pillow
```

سپس برنامه را اجرا کنید:

```bash
python main.py
```

> نام فایل اصلی اجرای برنامه ممکن است با تغییر ساختار پروژه تغییر کند.

---

## ⚠️ نکته مهم

Gaming DNS Optimizer یک **ابزار تست و مدیریت DNS** است.

تغییر DNS به معنی افزایش مستقیم سرعت اینترنت یا تضمین کاهش Ping داخل بازی نیست.

نتیجه واقعی به ISP، مسیر شبکه، موقعیت کاربر، وضعیت DNS و سرور مقصد بستگی دارد.

برای نتیجه قابل‌اعتمادتر، بهتر است DNSها را در چند نوبت مختلف تست کرده و نتایج History را با یکدیگر مقایسه کنید.

---

## 🔐 حریم خصوصی

تنظیمات، تاریخچه تست‌ها و اطلاعات مربوط به Activity برنامه به صورت محلی روی سیستم ویندوز کاربر نگهداری می‌شوند.

---

## 🧰 ساخته‌شده با

- 🐍 Python
- 🖥️ CustomTkinter
- Tkinter
- Windows `ping`
- Windows `nslookup`
- Windows `netsh`
- JSON
- Threading / ThreadPoolExecutor

---

## 🎮 مناسب چه کسانی است؟

این برنامه برای موارد زیر ساخته شده است:

- گیمرهای PC
- افرادی که می‌خواهند DNSهای مختلف را مقایسه کنند
- کاربرانی که با مشکلات DNS مواجه هستند
- افرادی که یک ابزار گرافیکی برای مدیریت DNS می‌خواهند
- گیمرهایی که می‌خواهند DNS را از طریق اینترنت خودشان تست کنند
- کاربرانی که می‌خواهند نتایج تست‌های قبلی را ذخیره و مقایسه کنند

---

## 📸 Screenshots

در این قسمت تصاویر برنامه قرار می‌گیرند.

پیشنهاد می‌شود از این بخش‌ها Screenshot بگیرید:

1. DNS Latency Test
2. DNS Speed Test
3. Analytics
4. Game Profiles
5. Settings
6. Activity Logs

---

## 🗺️ Roadmap

قابلیت‌هایی که می‌توانند در نسخه‌های آینده اضافه شوند:

- [ ] پیشنهاد خودکار بهترین DNS
- [ ] ابزارهای پیشرفته‌تر Network Diagnostics
- [ ] تست اختصاصی برای بازی‌ها
- [ ] نمودارهای حرفه‌ای Performance
- [ ] مانیتورینگ در پس‌زمینه
- [ ] سیستم امتیازدهی قابل تنظیم
- [ ] Import / Export کتابخانه DNS
- [ ] پشتیبانی چندزبانه
- [ ] Installer حرفه‌ای ویندوز
- [ ] سیستم آپدیت خودکار

---

## 👤 Developer

**RF020**

GitHub: `rf02076`

Telegram: `@RF020`

---

## ☕ Support

اگر Gaming DNS Optimizer برای شما مفید بود:

⭐ به Repository ستاره بدهید  
🐛 باگ‌ها را گزارش کنید  
💡 پیشنهادهای خود را ارسال کنید  
🔧 در توسعه پروژه مشارکت کنید

---

# ⚡ Gaming DNS Optimizer

**Test. Compare. Optimize.**

**تست کن • مقایسه کن • بهینه کن**

Made with 🐍 Python by **RF020**
