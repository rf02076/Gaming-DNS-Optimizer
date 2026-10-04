import customtkinter as ctk
import subprocess
import re
import threading
import json
import os
import sys
import time
import urllib.request
import webbrowser
from urllib.parse import urlparse

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ICON_FILE = "PD.ico"

# --- اصلاح مشکل دسترسی فایل کانفیگ در ویندوز ---
# ذخیره تنظیمات در مسیر AppData کاربر تا با ارور دسترسی (Permission Denied) مواجه نشیم
APP_DATA_DIR = os.path.join(os.getenv('APPDATA', os.path.expanduser('~')), 'Gaming_DNS_Optimizer')
if not os.path.exists(APP_DATA_DIR):
    os.makedirs(APP_DATA_DIR)
CONFIG_FILE = os.path.join(APP_DATA_DIR, "config.json")
# ------------------------------------------------

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class GameDNSApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gaming DNS Optimizer")
        self.geometry("800x870")
        self.resizable(True, True)
        
        icon_path = resource_path(ICON_FILE)
        if os.path.exists(icon_path):
            try: self.iconbitmap(icon_path); self.wm_iconbitmap(icon_path)
            except: pass

        self.best_dns_data = None
        self.tabview = ctk.CTkTabview(self, width=760, height=790)
        self.tabview.pack(padx=15, pady=(15, 0))

        self.tab_test = self.tabview.add("⚡ DNS Latency Test")
        self.tab_speed = self.tabview.add("🌐 DNS Speed Test")
        self.tab_profiles = self.tabview.add("🎯 Profiles")
        self.tab_settings = self.tabview.add("⚙ Settings")

        self.load_config()
        self.setup_test_tab()
        self.setup_speed_tab()
        self.setup_profiles_tab()
        self.setup_settings_tab()

        # فریم پایین برای واترمارک و دونیت
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(pady=(5, 10))

        self.watermark_label = ctk.CTkLabel(bottom_frame, text="Created By @RF020", font=("Segoe UI", 10), text_color="#475569", cursor="arrow")
        self.watermark_label.pack(side="left", padx=(0, 20))
        self.watermark_label.bind("<Enter>", lambda e: self.watermark_label.configure(text_color="#ffffff", cursor="hand2"))
        self.watermark_label.bind("<Leave>", lambda e: self.watermark_label.configure(text_color="#475569", cursor="arrow"))
        self.watermark_label.bind("<Button-1>", lambda e: webbrowser.open("https://t.me/RF020"))

        self.donate_label = ctk.CTkLabel(bottom_frame, text="☕ Donate us", font=("Segoe UI", 10, "bold"), text_color="#f59e0b", cursor="arrow")
        self.donate_label.pack(side="left")
        self.donate_label.bind("<Enter>", lambda e: self.donate_label.configure(text_color="#ffffff", cursor="hand2"))
        self.donate_label.bind("<Leave>", lambda e: self.donate_label.configure(text_color="#f59e0b", cursor="arrow"))
        self.donate_label.bind("<Button-1>", lambda e: webbrowser.open("https://donofa.ir/RF020/"))

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f: self.config = json.load(f)
            if "profiles" not in self.config: self.config["profiles"] = []
            if "speed_links" not in self.config: self.config["speed_links"] = ["http://speedtest.tele2.net/10MB.zip"]
        else:
            self.config = {
                "speed_links": ["http://speedtest.tele2.net/10MB.zip"],
                "profiles": [],
                "dns_list": [
                    {"category": "Gaming IR", "name": "Electro Gaming", "ip1": "78.157.42.101", "ip2": "78.157.42.100"},
                    {"category": "Gaming IR", "name": "Zenus Gaming", "ip1": "37.32.5.61", "ip2": "37.32.5.60"},
                    {"category": "Gaming IR", "name": "Radar Gaming", "ip1": "10.202.10.11", "ip2": "10.202.10.10"},
                    {"category": "Gaming IR", "name": "Vanil Gaming", "ip1": "10.139.177.22", "ip2": "10.139.177.21"},
                    {"category": "Foreign Gaming", "name": "Cloudflare", "ip1": "1.1.1.1", "ip2": "1.0.0.1"},
                    {"category": "Foreign Gaming", "name": "Google DNS", "ip1": "8.8.8.8", "ip2": "8.8.4.4"},
                    {"category": "Foreign Gaming", "name": "Quad9", "ip1": "9.9.9.9", "ip2": "149.112.112.112"},
                    {"category": "Foreign Gaming", "name": "OpenDNS", "ip1": "208.67.222.222", "ip2": "208.67.220.220"},
                    {"category": "Foreign Gaming", "name": "NextDNS", "ip1": "45.90.28.0", "ip2": "45.90.30.0"},
                    {"category": "Foreign Gaming", "name": "Yandex DNS", "ip1": "77.88.8.8", "ip2": "77.88.8.1"},
                    {"category": "Foreign Gaming", "name": "Neustar", "ip1": "156.154.70.1", "ip2": "156.154.71.1"},
                    {"category": "Foreign Gaming", "name": "DNS Alternatif", "ip1": "76.76.19.19", "ip2": "76.223.122.150"},
                    {"category": "Anti-Filter", "name": "Shecan (شکن)", "ip1": "178.22.122.100", "ip2": "185.51.200.2"},
                    {"category": "Anti-Filter", "name": "Begzar (بگذر)", "ip1": "185.55.226.26", "ip2": "185.55.225.25"},
                    {"category": "Anti-Filter", "name": "Electro (الکترو)", "ip1": "78.157.42.100", "ip2": "78.157.42.101"},
                    {"category": "Anti-Filter", "name": "Radar (رادار)", "ip1": "10.202.10.10", "ip2": "10.202.10.11"},
                    {"category": "Anti-Filter", "name": "Vanil (وایند)", "ip1": "10.139.177.21", "ip2": "10.139.177.22"},
                    {"category": "Anti-Filter", "name": "Zenus (زنوس)", "ip1": "37.32.5.60", "ip2": "37.32.5.61"},
                    {"category": "Anti-Filter", "name": "403.online", "ip1": "10.202.10.202", "ip2": "10.202.10.102"},
                    {"category": "Security", "name": "AdGuard DNS", "ip1": "94.140.14.14", "ip2": "94.140.15.15"},
                    {"category": "Security", "name": "Control D", "ip1": "76.76.2.0", "ip2": "76.76.10.0"},
                    {"category": "Security", "name": "CleanBrowsing", "ip1": "185.228.168.9", "ip2": "185.228.169.9"},
                    {"category": "Security", "name": "SafeDNS", "ip1": "195.46.39.39", "ip2": "195.46.39.40"},
                    {"category": "Security", "name": "Cisco Umbrella", "ip1": "208.67.222.220", "ip2": "208.67.222.222"},
                    {"category": "Security", "name": "IBM Quad9", "ip1": "9.9.9.10", "ip2": "149.112.112.10"},
                    {"category": "Security", "name": "Comodo Secure", "ip1": "8.26.56.26", "ip2": "8.20.247.20"},
                    {"category": "Security", "name": "FreeDNS", "ip1": "37.235.1.174", "ip2": "37.235.1.177"},
                    {"category": "Security", "name": "Alternate DNS", "ip1": "76.76.19.19", "ip2": "76.223.122.150"},
                    {"category": "Standard", "name": "Hurricane Electric", "ip1": "74.82.42.42", "ip2": "74.82.42.43"},
                    {"category": "Standard", "name": "DynDNS", "ip1": "216.146.35.35", "ip2": "216.146.36.36"},
                    {"category": "Standard", "name": "CenturyLink", "ip1": "205.171.3.25", "ip2": "205.171.2.65"},
                    {"category": "Standard", "name": "AirVPN DNS", "ip1": "10.4.0.1", "ip2": "10.5.0.1"},
                    {"category": "Standard", "name": "PrivDNS", "ip1": "212.112.112.113", "ip2": ""},
                    {"category": "Standard", "name": "DNS.WATCH", "ip1": "84.200.69.80", "ip2": "84.200.70.40"},
                    {"category": "Standard", "name": "Verisign", "ip1": "64.6.64.6", "ip2": "64.6.65.6"},
                    {"category": "Standard", "name": "Level3", "ip1": "4.2.2.1", "ip2": "4.2.2.2"}
                ]
            }
            self.save_config()

    def save_config(self):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f: json.dump(self.config, f, indent=4)

    def get_adapters(self):
        try:
            result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True, creationflags=0x08000000)
            return [line.split()[3] for line in result.stdout.split('\n') if "Connected" in line and len(line.split()) >= 4] or ["Ethernet"]
        except: return ["Ethernet"]

    def get_categories(self): return ["All"] + list(set([d["category"] for d in self.config["dns_list"]]))
    def get_dns_names(self): return [f"{d['name']} ({d['ip1']})" for d in self.config["dns_list"]]
    def get_filtered_dns(self, combo): 
        cat = combo.get()
        return self.config["dns_list"] if cat == "All" else [d for d in self.config["dns_list"] if d["category"] == cat]

    def apply_dns(self, ip1, ip2, status_label=None):
        adapter = self.adapter_combo.get()
        try:
            subprocess.run(f'netsh interface ip set dns "{adapter}" static {ip1} primary', shell=True, creationflags=0x08000000)
            if ip2: subprocess.run(f'netsh interface ip add dns "{adapter}" {ip2} index=2', shell=True, creationflags=0x08000000)
            subprocess.run('ipconfig /flushdns', shell=True, creationflags=0x08000000)
            if status_label: status_label.configure(text=f"✅ {ip1} Applied & Flushed!", text_color="#22c55e")
            return True
        except:
            if status_label: status_label.configure(text="❌ Error! Run as Admin.", text_color="#ef4444")
            return False

    # ========================================== تب 1: تست تاخیر ==========================================
    def setup_test_tab(self):
        top = ctk.CTkFrame(self.tab_test, fg_color="transparent"); top.pack(fill="x", padx=15, pady=(10, 5))
        ctk.CTkLabel(top, text="Adapter:", font=("Segoe UI", 13)).pack(side="left", padx=5)
        self.adapter_combo = ctk.CTkComboBox(top, values=self.get_adapters(), width=150, font=("Segoe UI", 12))
        self.adapter_combo.pack(side="left", padx=5)
        ctk.CTkLabel(top, text="Category:", font=("Segoe UI", 13)).pack(side="left", padx=(20,5))
        self.ping_cat_combo = ctk.CTkComboBox(top, values=self.get_categories(), width=150, font=("Segoe UI", 12))
        self.ping_cat_combo.set("All"); self.ping_cat_combo.pack(side="left", padx=5)
        ctk.CTkLabel(top, text="Mode:", font=("Segoe UI", 13)).pack(side="left", padx=(20,5))
        self.mode_combo = ctk.CTkComboBox(top, values=["Fast", "Medium", "Optimal"], width=120, font=("Segoe UI", 12))
        self.mode_combo.set("Optimal"); self.mode_combo.pack(side="left", padx=5)

        manual_frame = ctk.CTkFrame(self.tab_test, fg_color="#1e293b", corner_radius=10)
        manual_frame.pack(fill="x", padx=15, pady=5)
        ctk.CTkLabel(manual_frame, text="Manual Target (IP/Domain):", font=("Segoe UI", 12), text_color="#94a3b8").pack(side="left", padx=(15,5), pady=8)
        self.manual_target_entry = ctk.CTkEntry(manual_frame, width=250, font=("Segoe UI", 12), placeholder_text="e.g. 162.249.72.0 (LoL EU)")
        self.manual_target_entry.pack(side="left", padx=5, pady=8)
        ctk.CTkButton(manual_frame, text="🎯 Ping Target", fg_color="#f59e0b", hover_color="#d97706", width=120, font=("Segoe UI", 11, "bold"), command=self.ping_custom_target).pack(side="left", padx=15, pady=8)

        btn = ctk.CTkFrame(self.tab_test, fg_color="transparent"); btn.pack(pady=10)
        self.test_btn = ctk.CTkButton(btn, text="🚀 Start DNS Test", command=self.start_dns_test, font=("Segoe UI", 14, "bold"), fg_color="#3b82f6", hover_color="#2563eb", width=250)
        self.test_btn.pack(side="left", padx=10)
        self.apply_best_btn = ctk.CTkButton(btn, text="⭐ Apply Best DNS", command=self.apply_best_dns, font=("Segoe UI", 14, "bold"), fg_color="#16a34a", hover_color="#15803d", width=250, state="disabled")
        self.apply_best_btn.pack(side="left", padx=10)

        self.progress_bar = ctk.CTkProgressBar(self.tab_test, width=730, height=8); self.progress_bar.pack(pady=5); self.progress_bar.set(0)
        self.ping_status = ctk.CTkLabel(self.tab_test, text="Ready - Finds the lowest ping DNS", font=("Segoe UI", 11), text_color="#94a3b8"); self.ping_status.pack()

        self.results_frame = ctk.CTkScrollableFrame(self.tab_test, width=730, height=460)
        self.results_frame.pack(pady=10, fill="both", expand=True, padx=15)

    def ping_custom_target(self):
        target = self.manual_target_entry.get().strip()
        if not target: return
        self.ping_status.configure(text=f"Pinging {target}...")
        threading.Thread(target=self._run_custom_ping, args=(target,), daemon=True).start()

    def _run_custom_ping(self, target):
        data = self.ping_host(target, 10)
        data["status"] = "CUSTOM"
        card = ctk.CTkFrame(self.results_frame, fg_color="#1e293b", corner_radius=10, border_width=2, border_color="#f59e0b")
        card.pack(pady=6, fill="x", padx=5, before=self.results_frame.winfo_children()[0] if self.results_frame.winfo_children() else None)
        hdr = ctk.CTkFrame(card, fg_color="transparent"); hdr.pack(fill="x", padx=15, pady=10)
        ctk.CTkLabel(hdr, text=f"🎯 {target}", font=("Segoe UI", 13, "bold"), text_color="#fbbf24").pack(side="left")
        ctk.CTkLabel(hdr, text=f"  CUSTOM  ", font=("Segoe UI", 11, "bold"), text_color="#000", fg_color="#f59e0b", corner_radius=5).pack(side="right", padx=5)
        ctk.CTkLabel(hdr, text=f"Loss: {data['loss']}", font=("Segoe UI", 11), text_color="#f87171").pack(side="right", padx=10)
        ctk.CTkLabel(hdr, text=f"Jitter: {data['jitter']}", font=("Segoe UI", 11), text_color="#fbbf24").pack(side="right", padx=10)
        ctk.CTkLabel(hdr, text=f"PING: {data['ping']}", font=("Segoe UI", 11), text_color="#60a5fa").pack(side="right", padx=10)
        self.ping_status.configure(text=f"Manual ping completed.", text_color="#22c55e")

    def apply_best_dns(self):
        if self.best_dns_data: self.apply_dns(self.best_dns_data['ip1'], self.best_dns_data['ip2'], self.ping_status)

    def start_dns_test(self):
        for w in self.results_frame.winfo_children(): w.destroy()
        self.best_dns_data = None; self.apply_best_btn.configure(state="disabled")
        self.test_btn.configure(state="disabled", text="Testing..."); self.progress_bar.set(0)
        threading.Thread(target=self.run_dns_test, daemon=True).start()

    def run_dns_test(self):
        count = 30 if self.mode_combo.get() == "Optimal" else (10 if self.mode_combo.get() == "Medium" else 4)
        dns_to_test = self.get_filtered_dns(self.ping_cat_combo)
        results = []
        for i, dns in enumerate(dns_to_test):
            self.progress_bar.set((i + 1) / len(dns_to_test))
            self.ping_status.configure(text=f"Pinging {dns['name']} ({i+1}/{len(dns_to_test)})...")
            results.append({"name": dns["name"], "category": dns["category"], "ip1": dns["ip1"], "ip2": dns["ip2"], "data": self.ping_host(dns["ip1"], count)})
        results.sort(key=lambda x: x["data"]["score"], reverse=True)
        if results: results[0]["data"]["status"] = "BEST"; self.best_dns_data = results[0]
        self.display_dns_results(results)
        self.ping_status.configure(text="DNS Test Completed!"); self.test_btn.configure(state="normal", text="🚀 Start DNS Test"); self.apply_best_btn.configure(state="normal")

    def ping_host(self, target_ip, count):
        try:
            process = subprocess.run(['ping', '-n', str(count), '-w', '1000', target_ip], capture_output=True, text=True, timeout=30, creationflags=0x08000000)
            loss = int(re.search(r'(\d+)% loss', process.stdout, re.IGNORECASE).group(1)) if re.search(r'(\d+)% loss', process.stdout) else 100
            pings = [int(t) for t in re.findall(r'time[=<](\d+)ms', process.stdout, re.IGNORECASE)]
            if not pings: return self.empty_data()
            avg = sum(pings)/len(pings)
            jitter = sum(abs(pings[i]-pings[i-1]) for i in range(1, len(pings)))/(len(pings)-1) if len(pings)>1 else 0
            pings_s = sorted(pings)
            p95 = pings_s[min(int(len(pings_s)*0.95), len(pings_s)-1)]
            p99 = pings_s[min(int(len(pings_s)*0.99), len(pings_s)-1)]
            score = max(0, min(100, 100 - (loss*4) - (jitter*2) - (avg*0.1)))
            return {"ping": f"{avg:.1f}ms", "jitter": f"{jitter:.1f}ms", "loss": f"{loss}%", "status": "POOR" if score<50 else ("GOOD" if score<80 else "EXCELLENT"), "score": int(score), "p95": f"{p95}ms", "p99": f"{p99}ms", "range": f"{min(pings)} - {max(pings)}ms", "bufferbloat": f"{jitter*1.5:.1f}ms", "consistency": f"{100 - (jitter*2):.1f}%", "packets": f"{len(pings)}/{count}"}
        except: return self.empty_data()

    def empty_data(self): return {"ping": "Timeout", "jitter": "0ms", "loss": "100%", "status": "POOR", "score": 0, "p95": "0ms", "p99": "0ms", "range": "0 - 0ms", "bufferbloat": "0ms", "consistency": "0%", "packets": "0/0"}

    def display_dns_results(self, results):
        colors = {"POOR": "#ef4444", "GOOD": "#eab308", "EXCELLENT": "#22c55e", "BEST": "#3b82f6"}
        for res in results:
            data = res["data"]; color = colors.get(data["status"], "#fff")
            card = ctk.CTkFrame(self.results_frame, fg_color="#1e293b", corner_radius=10, border_width=1, border_color="#334155")
            card.pack(pady=6, fill="x", padx=5)
            hdr = ctk.CTkFrame(card, fg_color="transparent"); hdr.pack(fill="x", padx=15, pady=10)
            ctk.CTkLabel(hdr, text=f"[{res['category']}] {res['name']}", font=("Segoe UI", 13, "bold"), text_color="#f8fafc").pack(side="left")
            def app_sp(ip1=res['ip1'], ip2=res['ip2']): self.apply_dns(ip1, ip2, self.ping_status)
            ctk.CTkButton(hdr, text="Apply", width=55, height=22, font=("Segoe UI", 10, "bold"), fg_color="#6366f1", hover_color="#4f46e5", command=app_sp).pack(side="right", padx=2)
            ctk.CTkLabel(hdr, text=f"  {data['status']}  ", font=("Segoe UI", 11, "bold"), text_color="#fff", fg_color=color, corner_radius=5).pack(side="right", padx=5)
            ctk.CTkLabel(hdr, text=f"Loss: {data['loss']}", font=("Segoe UI", 11), text_color="#f87171").pack(side="right", padx=10)
            ctk.CTkLabel(hdr, text=f"Jitter: {data['jitter']}", font=("Segoe UI", 11), text_color="#fbbf24").pack(side="right", padx=10)
            ctk.CTkLabel(hdr, text=f"PING: {data['ping']}", font=("Segoe UI", 11), text_color="#60a5fa").pack(side="right", padx=10)

            det = ctk.CTkFrame(card, fg_color="#0f172a", corner_radius=5)
            def toggle(f=det, d=data):
                if f.winfo_children():
                    for w in f.winfo_children(): w.destroy()
                    f.pack_forget()
                else:
                    for t, items in [("Latency Analysis", [("Median Ping", d["ping"]), ("P95/P99 Ping", f"{d['p95']} / {d['p99']}"), ("Range", d["range"])]), ("Bufferbloat & Stability", [("Bufferbloat", d["bufferbloat"]), ("Consistency", d["consistency"])]), ("Reliability & Loss", [("Packets", d["packets"]), ("Score", f"{d['score']}/100")])]:
                        s = ctk.CTkFrame(f, fg_color="transparent"); s.pack(fill="x", pady=2, padx=5)
                        ctk.CTkLabel(s, text=t, font=("Segoe UI", 11, "bold"), text_color="#cbd5e1").pack(anchor="w")
                        for lbl, val in items:
                            r = ctk.CTkFrame(f, fg_color="transparent"); r.pack(fill="x", padx=20)
                            ctk.CTkLabel(r, text=f"{lbl}:", font=("Segoe UI", 11), text_color="#64748b", width=120, anchor="w").pack(side="left")
                            ctk.CTkLabel(r, text=val, font=("Segoe UI", 11), text_color="#e2e8f0", anchor="w").pack(side="left")
                    f.pack(fill="x", padx=15, pady=(0, 10))
            ctk.CTkButton(hdr, text="More", width=45, height=22, font=("Segoe UI", 10), fg_color="transparent", hover_color="#334155", text_color="#94a3b8", command=toggle).pack(side="right")

    # ========================================== تب 2: تست سرعت ==========================================
    def setup_speed_tab(self):
        top = ctk.CTkFrame(self.tab_speed, fg_color="transparent"); top.pack(fill="x", padx=15, pady=10)
        ctk.CTkLabel(top, text="Adapter:", font=("Segoe UI", 13)).pack(side="left", padx=5)
        self.speed_adapter_combo = ctk.CTkComboBox(top, values=self.get_adapters(), width=150, font=("Segoe UI", 12))
        self.speed_adapter_combo.pack(side="left", padx=5)
        ctk.CTkLabel(top, text="Category:", font=("Segoe UI", 13)).pack(side="left", padx=(20,5))
        self.speed_cat_combo = ctk.CTkComboBox(top, values=self.get_categories(), width=150, font=("Segoe UI", 12))
        self.speed_cat_combo.set("All"); self.speed_cat_combo.pack(side="left", padx=5)
        ctk.CTkLabel(top, text="Mode:", font=("Segoe UI", 13)).pack(side="left", padx=(20,5))
        self.speed_mode_combo = ctk.CTkComboBox(top, values=["Fast (1MB)", "Medium (3MB)", "Optimal (5MB)"], width=120, font=("Segoe UI", 12))
        self.speed_mode_combo.set("Fast (1MB)"); self.speed_mode_combo.pack(side="left", padx=5)

        link_frame = ctk.CTkFrame(self.tab_speed, fg_color="#1e293b", corner_radius=10); link_frame.pack(fill="x", padx=15, pady=5)
        row0 = ctk.CTkFrame(link_frame, fg_color="transparent"); row0.pack(fill="x", padx=15, pady=(10,5))
        ctk.CTkLabel(row0, text="Test Link:", font=("Segoe UI", 13)).pack(side="left", padx=5)
        self.speed_link_combo = ctk.CTkComboBox(row0, values=self.config.get("speed_links", []), width=400, font=("Segoe UI", 12))
        self.speed_link_combo.pack(side="left", padx=5)
        ctk.CTkButton(row0, text="🗑 Delete", width=70, fg_color="#dc2626", hover_color="#b91c1c", command=self.del_speed_link).pack(side="left", padx=5)
        
        row1 = ctk.CTkFrame(link_frame, fg_color="transparent"); row1.pack(fill="x", padx=15, pady=(0,10))
        self.new_link_entry = ctk.CTkEntry(row1, width=500, font=("Segoe UI", 12), placeholder_text="Use Direct IP links (e.g. http://1.1.1.1/file.zip) to avoid changing DNS")
        self.new_link_entry.pack(side="left", padx=(5,5))
        ctk.CTkButton(row1, text="Add Link", width=80, fg_color="#16a34a", hover_color="#15803d", command=self.add_speed_link).pack(side="left")

        btn_frame = ctk.CTkFrame(self.tab_speed, fg_color="transparent"); btn_frame.pack(pady=10)
        self.speed_btn = ctk.CTkButton(btn_frame, text="🌐 Start Speed Test", command=self.start_speed_test, font=("Segoe UI", 14, "bold"), fg_color="#8b5cf6", hover_color="#7c3aed", width=280)
        self.speed_btn.pack(side="left", padx=10)
        self.apply_best_speed_btn = ctk.CTkButton(btn_frame, text="⭐ Apply Best DNS", command=self.apply_best_speed_dns, font=("Segoe UI", 14, "bold"), fg_color="#16a34a", hover_color="#15803d", width=220, state="disabled")
        self.apply_best_speed_btn.pack(side="left", padx=10)

        self.speed_progress = ctk.CTkProgressBar(self.tab_speed, width=730, height=8); self.speed_progress.pack(pady=5); self.speed_progress.set(0)
        self.speed_status = ctk.CTkLabel(self.tab_speed, text="Ready", font=("Segoe UI", 11), text_color="#94a3b8"); self.speed_status.pack()

        self.speed_results_frame = ctk.CTkScrollableFrame(self.tab_speed, width=730, height=400)
        self.speed_results_frame.pack(pady=10, fill="both", expand=True, padx=15)

    def add_speed_link(self):
        link = self.new_link_entry.get().strip()
        if link and link not in self.config["speed_links"]:
            self.config["speed_links"].append(link); self.save_config()
            self.speed_link_combo.configure(values=self.config["speed_links"]); self.speed_link_combo.set(link); self.new_link_entry.delete(0, "end")

    def del_speed_link(self):
        sel = self.speed_link_combo.get()
        if sel in self.config["speed_links"]:
            self.config["speed_links"].remove(sel); self.save_config()
            self.speed_link_combo.configure(values=self.config["speed_links"])
            if self.config["speed_links"]: self.speed_link_combo.set(self.config["speed_links"][0])
            else: self.speed_link_combo.set("")

    def apply_best_speed_dns(self):
        if self.best_speed_data: self.apply_dns(self.best_speed_data['ip1'], self.best_speed_data['ip2'], self.speed_status)

    def start_speed_test(self):
        for w in self.speed_results_frame.winfo_children(): w.destroy()
        self.best_speed_data = None; self.apply_best_speed_btn.configure(state="disabled")
        self.speed_btn.configure(state="disabled", text="Testing..."); self.speed_progress.set(0)
        threading.Thread(target=self.run_speed_test, daemon=True).start()

    def run_speed_test(self):
        mode = self.speed_mode_combo.get()
        limit_bytes = 1*1024*1024 if "1MB" in mode else (3*1024*1024 if "3MB" in mode else 5*1024*1024)
        link = self.speed_link_combo.get()
        if not link.startswith("http"):
            self.speed_status.configure(text="Select a valid link.", text_color="#ef4444"); self.speed_btn.configure(state="normal", text="🌐 Start Speed Test"); return

        parsed = urlparse(link)
        is_ip_link = bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", parsed.hostname or ""))

        dns_to_test = self.get_filtered_dns(self.speed_cat_combo)
        results = []
        temp_adapter = self.adapter_combo.get()
        self.adapter_combo.set(self.speed_adapter_combo.get())

        for i, dns in enumerate(dns_to_test):
            self.speed_progress.set((i + 1) / len(dns_to_test))
            
            if is_ip_link:
                self.speed_status.configure(text=f"[{i+1}/{len(dns_to_test)}] Testing {dns['name']} (Direct IP)...")
            else:
                self.speed_status.configure(text=f"[{i+1}/{len(dns_to_test)}] Applying {dns['name']}...")
                self.apply_dns(dns['ip1'], dns['ip2'])
                time.sleep(1.5)
            
            try:
                start = time.time(); downloaded = 0; chunk_size = 1024 * 100
                response = urllib.request.urlopen(link, timeout=15)
                while downloaded < limit_bytes:
                    chunk = response.read(chunk_size)
                    if not chunk: break 
                    downloaded += len(chunk)
                dur = time.time() - start; downloaded_mb = downloaded / (1024 * 1024)
                if dur > 0 and downloaded_mb > 0:
                    speed_mbps = (downloaded_mb * 8) / dur
                    results.append({"name": dns["name"], "category": dns["category"], "ip1": dns["ip1"], "ip2": dns["ip2"], "data": {"speed": f"{speed_mbps:.2f} Mbps", "time": f"{dur:.2f} s", "status": "BEST" if speed_mbps > 20 else ("GOOD" if speed_mbps > 5 else "POOR"), "score": int(speed_mbps * 2)}})
                else: raise Exception("No data")
            except:
                results.append({"name": dns["name"], "category": dns["category"], "ip1": dns["ip1"], "ip2": dns["ip2"], "data": {"speed": "Fail", "time": "-", "status": "POOR", "score": 0}})

        self.adapter_combo.set(temp_adapter)
        results.sort(key=lambda x: x["data"]["score"], reverse=True)
        if results: results[0]["data"]["status"] = "BEST"; self.best_speed_data = results[0]
        
        self.display_speed_results(results)
        self.speed_status.configure(text="Speed Test Completed!"); self.speed_btn.configure(state="normal", text="🌐 Start Speed Test"); self.apply_best_speed_btn.configure(state="normal")

    def display_speed_results(self, results):
        colors = {"POOR": "#ef4444", "GOOD": "#eab308", "BEST": "#3b82f6"}
        for res in results:
            data = res["data"]; color = colors.get(data["status"], "#fff")
            card = ctk.CTkFrame(self.speed_results_frame, fg_color="#1e293b", corner_radius=10, border_width=1, border_color="#334155")
            card.pack(pady=6, fill="x", padx=5)
            hdr = ctk.CTkFrame(card, fg_color="transparent"); hdr.pack(fill="x", padx=15, pady=10)
            ctk.CTkLabel(hdr, text=f"[{res['category']}] {res['name']}", font=("Segoe UI", 13, "bold"), text_color="#f8fafc").pack(side="left")
            def app_sp(ip1=res['ip1'], ip2=res['ip2']): self.apply_dns(ip1, ip2, self.speed_status)
            ctk.CTkButton(hdr, text="Apply", width=55, height=22, font=("Segoe UI", 10, "bold"), fg_color="#6366f1", hover_color="#4f46e5", command=app_sp).pack(side="right", padx=2)
            ctk.CTkLabel(hdr, text=f"  {data['status']}  ", font=("Segoe UI", 11, "bold"), text_color="#fff", fg_color=color, corner_radius=5).pack(side="right", padx=5)
            ctk.CTkLabel(hdr, text=f"Time: {data['time']}", font=("Segoe UI", 11), text_color="#fbbf24").pack(side="right", padx=10)
            ctk.CTkLabel(hdr, text=f"Speed: {data['speed']}", font=("Segoe UI", 11), text_color="#60a5fa").pack(side="right", padx=10)

    # ========================================== تب‌های پروفایل و تنظیمات ==========================================
    def setup_profiles_tab(self):
        ctk.CTkLabel(self.tab_profiles, text="Create one-click profiles for your games", font=("Segoe UI", 14), text_color="#94a3b8").pack(pady=(20,10))
        create_frame = ctk.CTkFrame(self.tab_profiles, fg_color="#1e293b", corner_radius=10); create_frame.pack(pady=10, fill="x", padx=20)
        ctk.CTkLabel(create_frame, text="Profile Name:", font=("Segoe UI", 13)).grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.prof_name = ctk.CTkEntry(create_frame, width=200, font=("Segoe UI", 12)); self.prof_name.grid(row=0, column=1, padx=5, pady=15)
        ctk.CTkLabel(create_frame, text="DNS 1:", font=("Segoe UI", 13)).grid(row=1, column=0, padx=15, pady=5, sticky="w")
        self.prof_dns1 = ctk.CTkComboBox(create_frame, values=self.get_dns_names(), width=300, font=("Segoe UI", 12)); self.prof_dns1.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        ctk.CTkLabel(create_frame, text="DNS 2:", font=("Segoe UI", 13)).grid(row=2, column=0, padx=15, pady=5, sticky="w")
        self.prof_dns2 = ctk.CTkComboBox(create_frame, values=self.get_dns_names(), width=300, font=("Segoe UI", 12)); self.prof_dns2.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        ctk.CTkButton(create_frame, text="Save Profile", fg_color="#16a34a", hover_color="#15803d", width=150, command=self.save_profile).grid(row=3, column=0, columnspan=3, pady=15)
        list_frame = ctk.CTkFrame(self.tab_profiles, fg_color="#1e293b", corner_radius=10); list_frame.pack(pady=10, fill="both", expand=True, padx=20)
        self.prof_list_frame = ctk.CTkScrollableFrame(list_frame, height=400); self.prof_list_frame.pack(pady=15, padx=15, fill="both", expand=True)
        self.refresh_profiles()

    def save_profile(self):
        name = self.prof_name.get()
        if not name: return
        ip1 = re.search(r'\((.*?)\)', self.prof_dns1.get()).group(1) if re.search(r'\((.*?)\)', self.prof_dns1.get()) else ""
        ip2 = re.search(r'\((.*?)\)', self.prof_dns2.get()).group(1) if re.search(r'\((.*?)\)', self.prof_dns2.get()) else ""
        self.config["profiles"].append({"name": name, "ip1": ip1, "ip2": ip2, "dns1_name": self.prof_dns1.get().split(" (")[0], "dns2_name": self.prof_dns2.get().split(" (")[0]})
        self.save_config(); self.prof_name.delete(0, "end"); self.refresh_profiles()

    def refresh_profiles(self):
        for w in self.prof_list_frame.winfo_children(): w.destroy()
        for p in self.config["profiles"]:
            row = ctk.CTkFrame(self.prof_list_frame, fg_color="#0f172a", corner_radius=8, border_width=1, border_color="#334155"); row.pack(fill="x", pady=5, padx=5)
            ctk.CTkLabel(row, text=f"🎮 {p['name']}", font=("Segoe UI", 14, "bold"), text_color="#f8fafc").pack(side="left", padx=15, pady=10)
            ctk.CTkLabel(row, text=f"1: {p['dns1_name']} | 2: {p['dns2_name']}", font=("Segoe UI", 11), text_color="#64748b").pack(side="left", padx=10)
            def apply_prof(ip1=p['ip1'], ip2=p['ip2']): self.apply_dns(ip1, ip2)
            ctk.CTkButton(row, text="⚡ Apply", width=80, font=("Segoe UI", 11, "bold"), fg_color="#3b82f6", hover_color="#2563eb", command=apply_prof).pack(side="right", padx=15, pady=10)
            def del_prof(name=p['name']):
                self.config["profiles"] = [pr for pr in self.config["profiles"] if pr["name"] != name]
                self.save_config(); self.refresh_profiles()
            ctk.CTkButton(row, text="🗑", width=30, fg_color="#dc2626", hover_color="#b91c1c", command=del_prof).pack(side="right", padx=5, pady=10)

    def setup_settings_tab(self):
        ui_frame = ctk.CTkFrame(self.tab_settings, fg_color="#1e293b", corner_radius=10); ui_frame.pack(fill="x", padx=15, pady=15)
        ctk.CTkLabel(ui_frame, text="UI Settings", font=("Segoe UI", 16, "bold"), text_color="#e0e0e0").pack(pady=15)
        row1 = ctk.CTkFrame(ui_frame, fg_color="transparent"); row1.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(row1, text="Theme:", font=("Segoe UI", 13), width=100, anchor="w").pack(side="left")
        ctk.CTkComboBox(row1, values=["Dark", "Light", "System"], width=200, command=lambda c: ctk.set_appearance_mode(c.lower())).pack(side="left")
        ctk.CTkLabel(row1, text="Res:", font=("Segoe UI", 13), width=50, anchor="w").pack(side="left", padx=(20,0))
        ctk.CTkComboBox(row1, values=["Default", "Compact", "Expanded"], width=150, command=lambda c: self.geometry("750x650" if c=="Compact" else ("900x900" if c=="Expanded" else "800x870"))).pack(side="left")

        dns_frame = ctk.CTkFrame(self.tab_settings, fg_color="#1e293b", corner_radius=10); dns_frame.pack(fill="both", expand=True, padx=15, pady=10)
        ctk.CTkLabel(dns_frame, text="Manage DNS Servers", font=("Segoe UI", 14, "bold"), text_color="#e0e0e0").pack(pady=15)
        grid_d = ctk.CTkFrame(dns_frame, fg_color="transparent"); grid_d.pack(pady=5, padx=15)
        ctk.CTkLabel(grid_d, text="Category:", font=("Segoe UI", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.d_cat_e = ctk.CTkEntry(grid_d, width=100); self.d_cat_e.grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkLabel(grid_d, text="Name:", font=("Segoe UI", 12)).grid(row=0, column=2, padx=5, pady=5)
        self.d_name_e = ctk.CTkEntry(grid_d, width=100); self.d_name_e.grid(row=0, column=3, padx=5, pady=5)
        ctk.CTkLabel(grid_d, text="IP 1:", font=("Segoe UI", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.d_ip1_e = ctk.CTkEntry(grid_d, width=120); self.d_ip1_e.grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkLabel(grid_d, text="IP 2:", font=("Segoe UI", 12)).grid(row=1, column=2, padx=5, pady=5)
        self.d_ip2_e = ctk.CTkEntry(grid_d, width=120); self.d_ip2_e.grid(row=1, column=3, padx=5, pady=5)
        ctk.CTkButton(grid_d, text="Add", width=60, fg_color="#16a34a", hover_color="#15803d", command=self.add_dns_ui).grid(row=0, column=4, rowspan=2, padx=10, pady=5)
        self.d_list = ctk.CTkTextbox(dns_frame, height=200, font=("Consolas", 11), fg_color="#0f172a"); self.d_list.pack(pady=10, padx=15, fill="both", expand=True); self.refresh_dns_ui()

    def refresh_dns_ui(self):
        self.d_list.delete("0.0", "end")
        for d in self.config["dns_list"]: self.d_list.insert("end", f"[{d['category']}] {d['name']}  ->  {d['ip1']} , {d['ip2']}\n")
        self.update_combos()

    def add_dns_ui(self):
        c, n, i1, i2 = self.d_cat_e.get(), self.d_name_e.get(), self.d_ip1_e.get(), self.d_ip2_e.get()
        if n and i1: self.config["dns_list"].append({"category": c, "name": n, "ip1": i1, "ip2": i2}); self.save_config(); self.refresh_dns_ui(); self.d_cat_e.delete(0, "end"); self.d_name_e.delete(0, "end"); self.d_ip1_e.delete(0, "end"); self.d_ip2_e.delete(0, "end")

    def update_combos(self):
        cats = self.get_categories()
        if hasattr(self, 'ping_cat_combo'): self.ping_cat_combo.configure(values=cats)
        if hasattr(self, 'speed_cat_combo'): self.speed_cat_combo.configure(values=cats)
        if hasattr(self, 'speed_link_combo'): self.speed_link_combo.configure(values=self.config.get("speed_links", []))
        if hasattr(self, 'prof_dns1'): self.prof_dns1.configure(values=self.get_dns_names())
        if hasattr(self, 'prof_dns2'): self.prof_dns2.configure(values=self.get_dns_names())

if __name__ == "__main__":
    app = GameDNSApp()
    app.mainloop()