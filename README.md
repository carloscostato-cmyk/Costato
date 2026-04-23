# O Mundo de Um Costato & Agente de RH Autônomo

Bem-vindo ao repositório central do site profissional e ecossistema de automação de carreira de **Carlos Costato**. 

Este projeto é dividido em duas partes principais: o **Portfólio Profissional (Elite Tech)** e o **Agente de RH Autônomo**.

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
