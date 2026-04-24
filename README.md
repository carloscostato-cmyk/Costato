# 🚀 Carlos Costato | Senior IT Project Manager & AI Specialist

[![Portfolio](https://img.shields.io/badge/Portfolio-Live-00f2fe?style=for-the-badge&logo=github&logoColor=white)](https://carloscostato-cmyk.github.io/Costato/)
[![Version 2.0](https://img.shields.io/badge/Version-2.0-purple?style=for-the-badge&logo=react&logoColor=white)](https://carloscostato-cmyk.github.io/Costato/ver2.html)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carlos-costato/)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:carlos.costato@gmail.com)

> **Enterprise IT Leadership & AI Innovation** | 15+ Anos de Experiência | Cybersecurity & Governance Specialist

## 🌐 Portfólio Profissional

**Site responsivo com design "Dark Mode Premium" focado em alta performance e impacto visual executivo.**

### 📱 Links Rápidos
- **🚀 Portfolio Principal:** [carloscostato-cmyk.github.io/Costato](https://carloscostato-cmyk.github.io/Costato/)
- **⚡ Version 2.0:** [carloscostato-cmyk.github.io/Costato/ver2.html](https://carloscostato-cmyk.github.io/Costato/ver2.html)
- **📄 CV Profissional:** [Gerador CV LinkedIn](https://carloscostato-cmyk.github.io/Costato/cv-pro.html)
- **📧 Contato Direto:** [Formulário Profissional](https://carloscostato-cmyk.github.io/Costato/contact.html)

### 🎯 Áreas de Atuação
- **🔒 Cybersecurity & Governance** - Frameworks de segurança e compliance
- **📊 Business Intelligence** - Dashboards Power BI para diretoria
- **🤖 Inteligência Artificial** - Modelos generativos e automação
- **🏢 SharePoint Enterprise** - Portais corporativos e gestão documental
- **⚙️ RPA & Automação** - Processos automatizados e eficiência operacional

### 📋 Páginas do Site
- `index.html` — Landing page com métricas executivas
- `services.html` — Áreas de atuação técnica detalhadas
- `experience.html` — Histórico profissional e certificações FIAP
- `portfolio.html` — Vitrine de projetos enterprise
- `cv-pro.html` — Gerador de currículo otimizado estilo LinkedIn
- `about.html` — Sobre e filosofia profissional
- `contact.html` — Contato direto com integração WhatsApp

---

## 🌐 1. Portfólio Profissional (O Mundo de Um Costato)

Um site estático responsivo, com design "Dark Mode Premium" e foco em alta performance e impacto visual executivo.

- **URL Pública:** [https://carloscostato-cmyk.github.io/Costato/](https://carloscostato-cmyk.github.io/Costato/)
- **Páginas Incluídas:**
  - `index.html` — Landing page de alto impacto e métricas executivas.
  - `services.html` — Áreas de atuação técnica.
  - `experience.html` — Histórico profissional e certificações.
  - `portfolio.html` — Vitrine de projetos.
  - `cv-pro.html` — Gerador de currículo otimizado no estilo LinkedIn (imprimível via `Ctrl+P`).
  - `about.html`, `contact.html` — Sobre e contato.

---

## 🤖 2. Agente de RH Autônomo (Caçador de Vagas)

Um sistema Python rodando na nuvem via **GitHub Actions**, focado em prospectar vagas alinhadas ao perfil Sênior/IA/Cybersecurity, sem intervenção manual.

- **Dashboard ao Vivo:** [https://carloscostato-cmyk.github.io/Costato/agente_de_RH/](https://carloscostato-cmyk.github.io/Costato/agente_de_RH/)

### 🔄 Como o Fluxo Funciona (O Pipeline)

1. **Busca Automatizada (Scraping/APIs):** 
   O robô roda no GitHub Actions e pesquisa em portais (Remotive, Arbeitnow, etc.) usando palavras-chave pré-definidas (ex: *Project Manager*, *Cybersecurity*, *IA*).
   
2. **Sistema de Pontuação (Match Score):** 
   O robô lê a descrição de cada vaga e atribui uma nota (0 a 100). Vagas com menos de 36 pontos são descartadas.

3. **Notificação no Telegram (4x ao dia):** 
   O sistema dispara uma mensagem para o Telegram do Costato nos seguintes horários (Horário de Brasília - BRT):
   - 🕖 **09:00** (Manhã)
   - 🕛 **12:00** (Meio-dia)
   - 🕐 **13:00** (Tarde)
   - 🕕 **18:00** (Fim de Expediente)
   
   A mensagem contém um resumo das vagas, o % de match e o link direto de aplicação.

4. **Gerenciamento no Dashboard:**
   - As vagas encontradas ficam salvas em `agente_de_RH/applications.json`.
   - O Costato abre o **Dashboard ao Vivo** (pelo link do Telegram ou pelo Site).
   - Ao se candidatar (usando o link direto na vaga), ele clica no botão **"📝 Marcar Candidatura"** no Dashboard para salvar que já enviou currículo para aquela vaga (status salvo localmente).

### 🛠️ Arquivos do Agente
- `.github/workflows/hr_agent.yml`: O "cérebro" da automação e do agendamento (cron jobs).
- `agente_de_RH/rh_specialist.py`: Motor de busca, filtros e regras de pontuação.
- `agente_de_RH/telegram_notifier.py`: Classe responsável pelo disparo das mensagens formatadas para a API do Telegram.
- `agente_de_RH/index.html`: O Dashboard visual interativo (Vue/Vanilla).
- `agente_de_RH/applications.json`: Banco de dados persistente gerenciado pelo bot.

---

## ⚙️ Implantação & Dependências

1. O site está rodando estaticamente via **GitHub Pages**.
2. O bot de RH requer os seguintes **Secrets no GitHub** (`Settings > Secrets and variables > Actions`):
   - `TELEGRAM_BOT_TOKEN`: Token gerado pelo @BotFather.
   - `TELEGRAM_CHAT_ID`: ID do chat de destino do Costato.
3. Todo commit na branch `main` atualiza o site instantaneamente. A base de vagas (`applications.json`) é commitada de volta no repositório de forma silenciosa (`[skip ci]`) pelo bot.
