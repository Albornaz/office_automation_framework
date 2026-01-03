 
## 📦 Office Automation Framework (OAF)

[![CI Example](https://github.com/mscbuild/office_automation_framework/actions/workflows/main.yml/badge.svg)](https://github.com/mscbuild/office_automation_framework/actions/workflows/main.yml)

  <svg xmlns="http://www.w3.org/2000/svg" width="97.5" height="28" role="img" aria-label="PYTHON"><g shape-rendering="crispEdges"><rect width="97.5" height="28" fill="#3670a0"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="100"><image x="9" y="7" width="14" height="14" href="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjZmZkZDU0IiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+UHl0aG9uPC90aXRsZT48cGF0aCBkPSJNMTQuMjUuMThsLjkuMi43My4yNi41OS4zLjQ1LjMyLjM0LjM0LjI1LjM0LjE2LjMzLjEuMy4wNC4yNi4wMi4yLS4wMS4xM1Y4LjVsLS4wNS42My0uMTMuNTUtLjIxLjQ2LS4yNi4zOC0uMy4zMS0uMzMuMjUtLjM1LjE5LS4zNS4xNC0uMzMuMS0uMy4wNy0uMjYuMDQtLjIxLjAySDguNzdsLS42OS4wNS0uNTkuMTQtLjUuMjItLjQxLjI3LS4zMy4zMi0uMjcuMzUtLjIuMzYtLjE1LjM3LS4xLjM1LS4wNy4zMi0uMDQuMjctLjAyLjIxdjMuMDZIMy4xN2wtLjIxLS4wMy0uMjgtLjA3LS4zMi0uMTItLjM1LS4xOC0uMzYtLjI2LS4zNi0uMzYtLjM1LS40Ni0uMzItLjU5LS4yOC0uNzMtLjIxLS44OC0uMTQtMS4wNS0uMDUtMS4yMy4wNi0xLjIyLjE2LTEuMDQuMjQtLjg3LjMyLS43MS4zNi0uNTcuNC0uNDQuNDItLjMzLjQyLS4yNC40LS4xNi4zNi0uMS4zMi0uMDUuMjQtLjAxaC4xNmwuMDYuMDFoOC4xNnYtLjgzSDYuMThsLS4wMS0yLjc1LS4wMi0uMzcuMDUtLjM0LjExLS4zMS4xNy0uMjguMjUtLjI2LjMxLS4yMy4zOC0uMi40NC0uMTguNTEtLjE1LjU4LS4xMi42NC0uMS43MS0uMDYuNzctLjA0Ljg0LS4wMiAxLjI3LjA1em0tNi4zIDEuOThsLS4yMy4zMy0uMDguNDEuMDguNDEuMjMuMzQuMzMuMjIuNDEuMDkuNDEtLjA5LjMzLS4yMi4yMy0uMzQuMDgtLjQxLS4wOC0uNDEtLjIzLS4zMy0uMzMtLjIyLS40MS0uMDktLjQxLjA5em0xMy4wOSAzLjk1bC4yOC4wNi4zMi4xMi4zNS4xOC4zNi4yNy4zNi4zNS4zNS40Ny4zMi41OS4yOC43My4yMS44OC4xNCAxLjA0LjA1IDEuMjMtLjA2IDEuMjMtLjE2IDEuMDQtLjI0Ljg2LS4zMi43MS0uMzYuNTctLjQuNDUtLjQyLjMzLS40Mi4yNC0uNC4xNi0uMzYuMDktLjMyLjA1LS4yNC4wMi0uMTYtLjAxaC04LjIydi44Mmg1Ljg0bC4wMSAyLjc2LjAyLjM2LS4wNS4zNC0uMTEuMzEtLjE3LjI5LS4yNS4yNS0uMzEuMjQtLjM4LjItLjQ0LjE3LS41MS4xNS0uNTguMTMtLjY0LjA5LS43MS4wNy0uNzcuMDQtLjg0LjAxLTEuMjctLjA0LTEuMDctLjE0LS45LS4yLS43My0uMjUtLjU5LS4zLS40NS0uMzMtLjM0LS4zNC0uMjUtLjM0LS4xNi0uMzMtLjEtLjMtLjA0LS4yNS0uMDItLjIuMDEtLjEzdi01LjM0bC4wNS0uNjQuMTMtLjU0LjIxLS40Ni4yNi0uMzguMy0uMzIuMzMtLjI0LjM1LS4yLjM1LS4xNC4zMy0uMS4zLS4wNi4yNi0uMDQuMjEtLjAyLjEzLS4wMWg1Ljg0bC42OS0uMDUuNTktLjE0LjUtLjIxLjQxLS4yOC4zMy0uMzIuMjctLjM1LjItLjM2LjE1LS4zNi4xLS4zNS4wNy0uMzIuMDQtLjI4LjAyLS4yMVY2LjA3aDIuMDlsLjE0LjAxem0tNi40NyAxNC4yNWwtLjIzLjMzLS4wOC40MS4wOC40MS4yMy4zMy4zMy4yMy40MS4wOC40MS0uMDguMzMtLjIzLjIzLS4zMy4wOC0uNDEtLjA4LS40MS0uMjMtLjMzLS4zMy0uMjMtLjQxLS4wOC0uNDEuMDh6Ii8+PC9zdmc+"/><text transform="scale(.1)" x="587.5" y="175" textLength="535" fill="#fff" font-weight="bold">PYTHON</text></g></svg>

 

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
