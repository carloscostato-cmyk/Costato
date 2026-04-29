# 🤖 Agente Autônomo de Recrutamento

**Sistema inteligente de automação de candidaturas para Carlos Costato**

## 🎯 Objetivo

Encontrar, analisar e se candidatar automaticamente às vagas de emprego compatíveis com o perfil profissional de Senior IT Project Manager, maximizando as chances de conseguir entrevistas e propostas.

## 🚀 Funcionalidades

### 🔍 Busca Inteligente de Vagas
- **Plataformas:** LinkedIn, Gupy, Vagas.com.br, Indeed, Catho
- **Keywords:** Project Manager, Scrum Master, Cybersecurity, Power Platform, etc.
- **Filtros:** Senioridade, Localização (São Paulo/Remoto), Exclusão automática de níveis junior

### 📊 Análise de Compatibilidade
- **Score de 0-100** baseado em:
  - Keywords no título (25 pontos)
  - Habilidades na descrição (15 pontos)
  - Senioridade compatível (20 pontos)
  - Localização adequada (15 pontos)
  - Penalização por níveis indesejados (-50 pontos)
- **Mínimo aceito:** 50 pontos

### ✨ Personalização Automática
- **3 templates** de carta de apresentação (escolha aleatória)
- **Adaptação do currículo** para cada vaga
- **Destaque de resultados** relevantes
- **Tom profissional e humanizado**

### 📋 Registro e Relatórios
- **JSON detalhado** de todas as candidaturas
- **CSV para análise** em Excel
- **Backup diário** automático
- **Status tracking** em tempo real

## 🛠️ Instalação e Configuração

### Pré-requisitos
```bash
# Python 3.8+
pip install -r requirements.txt

# Chrome WebDriver
# Baixar: https://chromedriver.chromium.org/
```

### Configuração
1. **Editar `config-agente.json`** com suas preferências
2. **Ajustar filtros** de busca conforme necessário
3. **Configurar limites** diários de aplicações

## 🚀 Execução

### Modo Simples
```bash
python agente-recrutamento.py
```

### Modo Avançado
```python
from agente_recrutamento import AgenteRecrutamento

# Criar instância
agente = AgenteRecrutamento()

# Executar missão completa
agente.executar_missao()

# Ou executar etapas específicas
agente.buscar_vagas_gupy()
agente.aplicar_vagas_top5()
agente.gerar_relatorio()
```

## 📊 Relatórios Gerados

### candidaturas.json
```json
{
  "data_aplicacao": "2024-04-27 14:30:00",
  "vaga": {
    "titulo": "Senior IT Project Manager",
    "empresa": "Tech Company",
    "plataforma": "LinkedIn",
    "score_compatibilidade": 85
  },
  "status": "Aplicada",
  "carta_apresentacao": "...",
  "curriculo_adaptado": "..."
}
```

### candidaturas.csv
| Data | Plataforma | Vaga | Empresa | Score | Status |
|------|------------|------|---------|-------|--------|
| 27/04/2024 | LinkedIn | Senior PM | Tech Corp | 85 | Aplicada |

## 🎯 Estratégias Implementadas

### 🧠 Inteligência Artificial
- **Análise de sentimento** das descrições
- **Extração automática** de habilidades
- **Predição de sucesso** da candidatura
- **Aprendizado** com feedback

### 🔒 Segurança e Performance
- **Rate limiting** para evitar bloqueios
- **User agents** rotativos
- **Proteção anti-bot**
- **Timeouts** e retries automáticos

### 📈 Otimização Contínua
- **A/B testing** de cartas
- **Análise de conversão**
- **Ajuste automático** de filtros
- **Melhoria de templates**

## 📋 Métricas de Sucesso

### 🎯 KPIs
- **Taxa de aplicação:** Vagas aplicadas / Vagas encontradas
- **Score médio:** Compatibilidade média das vagas
- **Taxa de resposta:** Entrevistas / Candidaturas
- **Tempo para resposta:** Dias até primeira entrevista

### 📊 Metas
- **50+ candidaturas** por semana
- **80+ score médio** de compatibilidade
- **10+ entrevistas** por mês
- **2+ propostas** por trimestre

## 🔧 Personalização

### Adicionar Novas Plataformas
```python
# Em config-agente.json
"nova_plataforma": {
  "url": "https://exemplo.com/",
  "ativa": true,
  "max_resultados": 20
}
```

### Customizar Templates
```python
# Em agente-recrutamento.py
templates = [
    "Seu template personalizado 1...",
    "Seu template personalizado 2...",
    "Seu template personalizado 3..."
]
```

### Ajustar Pesos de Compatibilidade
```json
// Em config-agente.json
"pesos": {
  "keywords_titulo": 30,  // Aumentado
  "senioridade": 25,      // Aumentado
  "localizacao": 10       // Reduzido
}
```

## 🚨 Segurança e Ética

### ⚠️ Importante
- **Respeitar limites** de cada plataforma
- **Não aplicar** para vagas incompatíveis
- **Personalizar genuinamente** cada candidatura
- **Manter qualidade** sobre quantidade

### 🛡️ Proteções
- **Validação SSL** em todas requisições
- **Rate limiting** automático
- **Detecção de CAPTCHAs**
- **Backup automático** de dados

## 📞 Suporte e Monitoramento

### 📈 Dashboard (Futuro)
- **Visualização em tempo real** de candidaturas
- **Gráficos de performance**
- **Alertas de oportunidades**
- **Análise de tendências**

### 🔔 Notificações
- **Telegram** para novas candidaturas
- **Email** para relatórios diários
- **Slack** para atualizações de status

## 🔄 Atualizações e Manutenção

### 📅 Rotina Semanal
1. **Analisar performance** das candidaturas
2. **Ajustar filtros** baseado em resultados
3. **Atualizar templates** com feedback
4. **Limpar logs** antigos

### 🚀 Roadmap
- [ ] **Integração com WhatsApp** para notificações
- [ ] **Machine Learning** para predição avançada
- [ ] **API REST** para integração externa
- [ ] **Dashboard web** para monitoramento
- [ ] **Multi-idioma** suporte

## 📄 Licença e Termos

Este agente foi desenvolvido especificamente para **Carlos Costato** e deve ser utilizado de forma ética e responsável, seguindo os termos de serviço de cada plataforma de vagas.

---

**🤖 Desenvolvido com ❤️ para maximizar suas oportunidades profissionais!**

**Portfolio:** https://carloscostato-cmyk.github.io/Costato/
