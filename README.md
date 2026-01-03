 
## 📦 Office Automation Framework (OAF)

![CI Example](https://github.com/mscbuild/office_automation_framework/actions/workflows/main.yml/badge.svg) 
 <img width="97" height="20" alt="image" src="https://github.com/user-attachments/assets/fd221c47-2431-4b99-bbd0-3eb867a4edec" />
 <img width="86" height="18" alt="image" src="https://github.com/user-attachments/assets/4b119585-4f1f-41b8-9eee-d87977c8e341" />



 
 

The Office Automation Framework (OAF) is an extensible Python framework for automating office tasks:

- 📊 Data processing,
- 📄 Report generation (HTML/PDF),
- 📬 Email distribution,
- 📁 File management,
- ⏰ Task scheduling,
- 🖥 CLI management.

**The framework is supplied as a pip package and can be used:**

- As a command-line utility

- As a library

- As a basis for a microservice or API

## 🎯 What is the project for?

In most companies:

- Reports are compiled manually

- Excel files are copied and edited manually

- PDF reports are not generated in a standardized manner

- Distribution is done manually

- There is no uniform reporting standard

❌ This leads to:

- errors

- wasted time

- lack of transparency

- difficulty scaling

**OAF solves these problems by providing a unified framework for automation.**

## 💡 Why do you need this particular framework?

| Problem | OAF Solution |
| ---------------------- | ------------------------- |
| Disjointed scripts | Unified architecture |
| No reporting standards | Jinja2 templates |
| Manual PDF export | HTML → PDF |
| No CLI | Full-fledged `oaf` command |
| Difficult to scale | Modular structure |
| No access roles | Access levels |

## 🗂 Project structure

~~~bash
office_automation_framework/
│
├── oaf/
│   ├── __init__.py
│   ├── config.py
│   ├── logging.py
│
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── processor.py
│   │   └── exporter.py
│
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── html.py
│   │   ├── pdf.py
│   │   └── templates/
│   │       └── financial_report_template.html
│
│   ├── files/
│   │   ├── __init__.py
│   │   └── manager.py
│
│   ├── mail/
│   │   ├── __init__.py
│   │   └── sender.py
│
│   ├── scheduler/
│   │   ├── __init__.py
│   │   └── scheduler.py
│
│   └── security/
│       ├── __init__.py
│       └── access.py
│
├── examples/
│   └── daily_financial_report.py
│
├── pyproject.toml
├── README.md
└── LICENSE
~~~

## 🏗 Project architecture

~~~bash
┌────────────┐
│ CLI (oaf)  │
└────┬───────┘
     │
┌────▼────────────┐
│ Business Logic  │
│ (reports, data) │
└────┬────────────┘
     │
┌────▼──────────────┐
│ Infrastructure    │
│ files, mail, pdf  │
└───────────── ─────┘
~~~

**The project is not tied to a UI, database, or web—it can be easily integrated into any environment.**

## 📌 C4 — Context Diagram

**Objective:** to show why the system exists and with whom it interacts.

~~~bash
┌──────────────────────────────┐
│        Business Users        │
│ (Finance, Analytics, HR)     │
└──────────────┬───────────────┘
               │ CLI / Reports
               ▼
┌─────────────────────────────────────┐
│   Office Automation Framework (OAF) │
│                                     │
│  • Data Processing                  │
│  • Reports (HTML / PDF)             │
│  • Scheduling                       │
│  • Email                            │
└──────────────┬───────────────┬──────┘
               │               │
               ▼               ▼
        ┌─────────────┐   ┌─────────────┐
        │ File System │   │ Email Server│
        │ CSV / Excel │   │ SMTP        │
        └─────────────┘   └─────────────┘
~~~

## 📦 C4 — Container Diagram

**Objective:** to show the main technical blocks.

~~~bash
┌───────────────────────────────────────────────┐
│                 CLI (oaf)                     │
│  argparse / entrypoints                       │
└───────────────┬───────────────────────────────┘
                ▼
┌───────────────────────────────────────────────┐
│            Core Application                   │
│                                               │
│  ┌────────────┐  ┌────────────┐  ┌─────────┐  │
│  │ Data Layer │  │ Report     │  │ Security│  │
│  │ (Pandas)   │  │ Engine     │  │ Access  │  │
│  └────────────┘  └────────────┘  └─────────┘  │
│                                               │
│  ┌────────────┐  ┌────────────┐               │
│  │ File Mgmt  │  │ Scheduler  │               │
│  │ os/shutil  │  │ schedule   │               │
│  └────────────┘  └────────────┘               │
└───────────────┬───────────────┬───────────────┘
                │               │
                ▼               ▼
         ┌────────────┐   ┌────────────┐
         │ PDF Engine │   │ Email SMTP │
         │ WeasyPrint│   │ smtplib     │ 
         └────────────┘   └────────────┘
~~~

## 🧱 C4 — Component 

~~~bash
Reports Module
┌──────────────────────────────────┐
│ HTMLReport                       │
│  • load template                 │
│  • render context                │
└───────────────┬──────────────────┘
                ▼
┌──────────────────────────────────┐
│ PDFReport                        │
│  • HTML → PDF                    │
└──────────────────────────────────┘

Data Module
┌────────────┐   ┌───────────────┐
│ DataLoader │ → │ DataProcessor │
└────────────┘   └───────────────┘
~~~

## 🔷 UML Component Diagram

~~~bash
+------------------+
|      CLI         |
+------------------+
          |
          v
+------------------+
| Report Service   |
+------------------+
 |        |        |
 v        v        v
Data   Templates  PDF
(Pandas) (Jinja2) (WeasyPrint)
~~~

## 🔁 UML Sequence Diagram (report generation)

~~~bash
User
 │
 │ oaf report generate
 ▼
CLI
 │ validate args
 │
 ▼
HTMLReport
 │ render template
 │
 ▼
PDFReport
 │ create PDF
 │
 ▼
FileSystem
 │ save report.pdf
 ▼
User
~~~

## 🧰 Tech Stack

🐍 Language

- Python 3.9+

## 📊 Data

- Pandas — loading, cleaning, and aggregating data

- OpenPyXL — Excel formatting

## 📄 Reports

- Jinja2 — HTML templates

- Chart.js — interactive charts

- WeasyPrint — HTML → PDF

## 📬 Mail

- smtplib

- email.message

## 📁 Files

- `os`, `shutil`

## ⏰ Planning

- schedule

## 🖥 CLI

- argparse

- pip entry points

## 🚀 Key Features

📊 Data Processing

- CSV / Excel

- Cleaning and Normalization

- Pivot Tables

- Aggregations

## 📄 Report generation

- HTML (corporate style)

- PDF (print, archive)

- Charts

- Multiple tables

- KPI blocks

## 🔐 Security

- Access levels:

- public

- internal

- confidential

- privacy warnings

- logical data isolation

## 🖥 CLI

~~~bash
oaf report generate
~~~

- Report parameters

- Templates

- Output files

- CI/CD ready

## 📬 Email

- Sending PDF

- Attachments

- SMTP Configuration

## ⏰ Planner

- Daily reports

- Automatic launch

 ## 🧪 Typical use cases

## 📅 Daily Reports

- Finance

- Sales

- HR

- Logistics

## 📈 Financial analytics

- P&L

- cash flow

- budgets

- variances

## 🗂 Archiving

- Daily PDF saving

- Date structure

## 🏢 Corporate reporting

- Unified style

- Unified templates

- Access control

## 🧩 Design for Extension

**OAF is designed from the ground up to grow.**

## 🔜 Possible additions

🔧 CLI

`oaf report email`

`oaf report schedule`

`oaf data validate`

🌐 Web / API

- FastAPI

- REST / GraphQL

- authorization

🐳 DevOps

- Docker

- Kubernetes CronJob

- GitHub Actions

🔐 Security

- PDF password

- watermark

- encryption

- RBAC

📊 BI

- Power BI

- Tableau

- unloading

🗄 Storage

- PostgreSQL

- S3 / MinIO

- SharePoint

## 📈 Business Benefits

- ⏱ Time Savings

- 📉 Error Reduction

- 📊 Transparent Analytics

- 🧩 Scalability

- 🔐 Security

- 🚀 Rapid Automation

## 🧠 Who is this project for?

- Python developers

- Analysts

- Finance departments

- IT departments

- DevOps

## 📦 Usage formats

| Format | Usage |
| ---------- | --------------------- |
| pip package | local scripts |
| CLI | automation |
| library | integration |
| service | enterprise systems |

## 🛠️ Installation

~~~bash
git clone https://github.com/mscbuild/office_automation_framework.git
cd office_automation_framework
~~~

## 🔹 Step 1: Clone or create a folder

~~~bash
mkdir office_automation_framework
cd office_automation_framework
~~~

## 🔹 Step 2: Install dependencies

~~~bash
pip install -r requirements.txt
~~~

## ⚠️ Additional for PDF (WeasyPrint) Windows

~~~bash
pip install weasyprint
~~~

## 🍎 macOS

~~~bash
brew install cairo pango gdk-pixbuf libffi
pip install weasyprint
~~~

## 🐧 Ubuntu / Debian

~~~bash
sudo apt install libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0
pip install weasyprint
~~~

## ▶ 2️⃣ Application (launch)

📊 Preparing Input Data

Create a file:
~~~bash
data/sales.xlsx
~~~

Columns:
~~~bash
manager | amount
~~~

## 🚀 Launch a daily report

~~~bash
python examples/daily_financial_report.py
~~~

## 📁 Result:

~~~bash
output/
├── summary.xlsx
└── report.pdf
~~~

**📧 The letter is sent automatically.**

## 🧪 3️⃣ Testing (simple)

🔹 Quick manual test
~~~bash
python -c "from oaf.data.loader import DataLoader; print(DataLoader)"
~~~

## 🔹 Testing report generation without email

(Temporarily comment out MailSender in daily_financial_report.py)
~~~bash
python examples/daily_financial_report.py
~~~

**Expected:**

- summary.xlsx

- report.pdf

## 🧪 4️⃣ Automated tests (optional, recommended)

Installing pytest
~~~bash
pip install pytest
~~~

Running tests
~~~bash
pytest
~~~

## 🔄 5️⃣ Typical developer workflow

~~~bash
git pull
source venv/bin/activate
pip install -r requirements.txt
pytest
python examples/daily_financial_report.py
~~~
 

## 📜 LICENSE (MIT)

MIT License
