#!/usr/bin/env python3
"""
🎯 GERENTE DE PROJETOS - Sistema de Feedback de Vagas
Carlos Costato - Sistema de Acompanhamento de Candidaturas
"""

import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import requests
import time
from bs4 import BeautifulSoup
import re

class GerenteFeedbackVagas:
    def __init__(self):
        self.config = {
            "email": "carlos.costato@gmail.com",
            "telefone": "+55 11 98639-5283",
            "linkedin": "https://www.linkedin.com/in/carlos-costato/",
            "portfolio": "https://carloscostato-cmyk.github.io/Costato/"
        }
        
        # Canais de feedback
        self.canais_feedback = {
            "email": True,
            "whatsapp": True,
            "linkedin": True,
            "dashboard": True,
            "relatorio_semanal": True
        }
        
        # Status das candidaturas
        self.status_workflow = {
            "aplicada": "Candidatura enviada",
            "visualizada": "Recrutador visualizou",
            "em_analise": "Em análise técnica",
            "entrevista_agendada": "Entrevista agendada", 
            "entrevista_realizada": "Entrevista realizada",
            "testes_solicitados": "Testes solicitados",
            "oferta_recebida": "Oferta recebida",
            "aceita": "Oferta aceita",
            "rejeitada": "Candidatura rejeitada",
            "sem_resposta": "Sem resposta"
        }
    
    def carregar_candidaturas(self):
        """Carrega candidaturas existentes"""
        try:
            with open('candidaturas.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except:
            return []
    
    def salvar_candidaturas(self, candidaturas):
        """Salva candidaturas atualizadas"""
        with open('candidaturas.json', 'w', encoding='utf-8') as f:
            json.dump(candidaturas, f, ensure_ascii=False, indent=2, default=str)
    
    def verificar_email_respostas(self):
        """Verifica respostas por email (simulação)"""
        print("Verificando respostas por email...")
        
        # Simulação - em produção seria integração com Gmail API
        respostas_simuladas = [
            {
                "vaga_id": 1,
                "empresa": "Tech Solutions Brasil",
                "assunto": "Re: Senior IT Project Manager - Sua Candidatura",
                "remetente": "recrutamento@techsolutions.com.br",
                "mensagem": "Prezado Carlos, recebemos sua candidatura e gostaríamos de agendar uma entrevista...",
                "data": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "tipo": "entrevista_agendada"
            },
            {
                "vaga_id": 3,
                "empresa": "Financial Services Corp",
                "assunto": "Status sua candidatura - Gerente de Projetos de TI",
                "remetente": "hr@financialservices.com",
                "mensagem": "Seu perfil foi selecionado para a próxima fase. Por favor, realize os testes técnicos...",
                "data": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "tipo": "testes_solicitados"
            }
        ]
        
        return respostas_simuladas
    
    def verificar_linkedin_mensagens(self):
        """Verifica mensagens no LinkedIn (simulação)"""
        print("Verificando mensagens no LinkedIn...")
        
        # Simulação - em produção seria LinkedIn API
        mensagens_simuladas = [
            {
                "vaga_id": 2,
                "empresa": "Digital Innovation Hub",
                "remetente": "Maria Silva - Tech Recruiter",
                "mensagem": "Olá Carlos! Vi seu perfil e gostaria de conversar sobre a vaga de Scrum Master...",
                "data": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "tipo": "contato_inicial"
            }
        ]
        
        return mensagens_simuladas
    
    def verificar_whatsapp_mensagens(self):
        """Verifica mensagens no WhatsApp (simulação)"""
        print("Verificando mensagens no WhatsApp...")
        
        # Simulação - em produção seria WhatsApp Business API
        mensagens_simuladas = [
            {
                "vaga_id": 5,
                "empresa": "Cloud Systems Integration",
                "remetente": "+55 11 99999-8888",
                "mensagem": "Olá Carlos, sou da Cloud Systems. Vi seu currículo e gostaria de conversar sobre a vaga...",
                "data": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "tipo": "contato_whatsapp"
            }
        ]
        
        return mensagens_simuladas
    
    def atualizar_status_candidaturas(self, respostas):
        """Atualiza status das candidaturas baseado nas respostas"""
        candidaturas = self.carregar_candidaturas()
        atualizacoes = []
        
        for resposta in respostas:
            # Encontrar candidatura correspondente
            for candidatura in candidaturas:
                if 'candidaturas' in candidatura:
                    for i, cand in enumerate(candidatura['candidaturas']):
                        if i == resposta['vaga_id']:
                            # Atualizar status
                            if 'status_atual' not in cand:
                                cand['status_atual'] = 'aplicada'
                            
                            # Mapear tipo de resposta para status
                            status_map = {
                                "contato_inicial": "visualizada",
                                "contato_whatsapp": "visualizada", 
                                "entrevista_agendada": "entrevista_agendada",
                                "testes_solicitados": "testes_solicitados",
                                "oferta_recebida": "oferta_recebida"
                            }
                            
                            novo_status = status_map.get(resposta['tipo'], resposta['tipo'])
                            cand['status_atual'] = novo_status
                            cand['ultima_atualizacao'] = resposta['data']
                            cand['feedback'] = resposta
                            
                            atualizacoes.append({
                                'vaga': cand['vaga']['titulo'],
                                'empresa': cand['vaga']['empresa'],
                                'status_anterior': 'aplicada',
                                'status_novo': novo_status,
                                'data': resposta['data'],
                                'mensagem': resposta['mensagem'][:100] + "..."
                            })
        
        if atualizacoes:
            self.salvar_candidaturas(candidaturas)
            print(f"{len(atualizacoes)} candidaturas atualizadas")
        
        return atualizacoes
    
    def enviar_notificacao_email(self, atualizacoes):
        """Envia notificação por email sobre atualizações"""
        if not atualizacoes:
            return
        
        print("Enviando notificacao por email...")
        
        # Configuração do servidor SMTP (simulação)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_user = self.config["email"]
        smtp_password = "sua_senha"  # Em produção usar app password
        
        # Criar mensagem
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = smtp_user
        msg['Subject'] = f"🎯 Feedback de Vagas - {len(atualizacoes)} Atualizações"
        
        # Corpo do email
        body = f"""
        <html>
        <body>
        <h2>🎯 Feedback de Vagas - Atualizações Recebidas</h2>
        <p>Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        <p>Total de atualizações: {len(atualizacoes)}</p>
        
        <h3>📋 Detalhes das Atualizações:</h3>
        <table border="1" style="border-collapse: collapse; width: 100%;">
        <tr style="background-color: #f0f0f0;">
        <th>Vaga</th>
        <th>Empresa</th>
        <th>Status Anterior</th>
        <th>Status Novo</th>
        <th>Data</th>
        <th>Mensagem</th>
        </tr>
        """
        
        for atualizacao in atualizacoes:
            body += f"""
        <tr>
        <td>{atualizacao['vaga']}</td>
        <td>{atualizacao['empresa']}</td>
        <td>{atualizacao['status_anterior']}</td>
        <td><strong>{atualizacao['status_novo']}</strong></td>
        <td>{atualizacao['data']}</td>
        <td>{atualizacao['mensagem']}</td>
        </tr>
        """
        
        body += f"""
        </table>
        
        <h3>🚀 Próximas Ações Recomendadas:</h3>
        <ul>
        <li>Responder aos recrutadores que entraram em contato</li>
        <li>Preparar-se para entrevistas agendadas</li>
        <li>Realizar testes técnicos solicitados</li>
        <li>Avaliar ofertas recebidas</li>
        </ul>
        
        <p><strong>Portfolio:</strong> <a href="{self.config['portfolio']}">carloscostato-cmyk.github.io/Costato/</a></p>
        <p><strong>LinkedIn:</strong> <a href="{self.config['linkedin']}">linkedin.com/in/carlos-costato/</a></p>
        
        <hr>
        <p><em>Este é um email automático do seu Sistema de Feedback de Vagas</em></p>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html', 'utf-8'))
        
        # Enviar email (simulação)
        try:
            # server = smtplib.SMTP(smtp_server, smtp_port)
            # server.starttls()
            # server.login(smtp_user, smtp_password)
            # server.send_message(msg)
            # server.quit()
            print("Email enviado com sucesso (simulado)")
        except Exception as e:
            print(f"❌ Erro ao enviar email: {e}")
    
    def enviar_notificacao_whatsapp(self, atualizacoes):
        """Envia notificação por WhatsApp"""
        if not atualizacoes:
            return
        
        print("Enviando notificacao por WhatsApp...")
        
        mensagem = f"""
        *Feedback de Vagas - {len(atualizacoes)} Atualizacoes*

        {datetime.now().strftime('%d/%m/%Y %H:%M')}

        *Resumo:*
        """
        
        for atualizacao in atualizacoes[:3]:  # Limitar a 3 para não exceder caractéres
            mensagem += f"""
        • {atualizacao['vaga']} - {atualizacao['empresa']}
        Status: {atualizacao['status_anterior']} -> {atualizacao['status_novo']}
        """
        
        mensagem += f"""
        
        *Acoes necessarias:*
        • Verificar detalhes no dashboard
        • Responder aos contatos recebidos
        • Preparar para proximas etapas

        *Dashboard:* {self.config['portfolio']}
        """
        
        # Gerar link WhatsApp
        whatsapp_url = f"https://wa.me/5511986395283?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
        
        print(f"Link WhatsApp gerado: {whatsapp_url}")
        print("Notificacao pronta para envio")
    
    def gerar_dashboard_feedback(self):
        """Gera dashboard HTML com feedback das vagas"""
        candidaturas = self.carregar_candidaturas()
        
        # Contagem por status
        status_count = {}
        for candidatura in candidaturas:
            if 'candidaturas' in candidatura:
                for cand in candidatura['candidaturas']:
                    status = cand.get('status_atual', 'aplicada')
                    status_count[status] = status_count.get(status, 0) + 1
        
        # Gerar HTML
        html_dashboard = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dashboard Feedback Vagas - Carlos Costato</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background: #f5f5f5;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .header {{
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .stats {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin-bottom: 30px;
                }}
                .stat-card {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                }}
                .stat-number {{
                    font-size: 2em;
                    font-weight: bold;
                    margin-bottom: 5px;
                }}
                .table-container {{
                    overflow-x: auto;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th, td {{
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background-color: #f8f9fa;
                    font-weight: bold;
                }}
                .status-aplicada {{ background-color: #e3f2fd; }}
                .status-visualizada {{ background-color: #fff3e0; }}
                .status-entrevista_agendada {{ background-color: #e8f5e8; }}
                .status-testes_solicitados {{ background-color: #fce4ec; }}
                .status-oferta_recebida {{ background-color: #f3e5f5; }}
                
                .refresh-btn {{
                    background: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    margin: 20px auto;
                    display: block;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎯 Dashboard Feedback Vagas</h1>
                    <p>Carlos Costato - Senior IT Project Manager</p>
                    <p>Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                </div>
                
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number">{len(candidaturas)}</div>
                        <div>Total Candidaturas</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{status_count.get('visualizada', 0)}</div>
                        <div>Visualizadas</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{status_count.get('entrevista_agendada', 0)}</div>
                        <div>Entrevistas</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{status_count.get('oferta_recebida', 0)}</div>
                        <div>Ofertas</div>
                    </div>
                </div>
                
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Vaga</th>
                                <th>Empresa</th>
                                <th>Plataforma</th>
                                <th>Data Aplicação</th>
                                <th>Status Atual</th>
                                <th>Última Atualização</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
        """
        
        for candidatura in candidaturas:
            if 'candidaturas' in candidatura:
                for cand in candidatura['candidaturas']:
                    status = cand.get('status_atual', 'aplicada')
                    html_dashboard += f"""
                            <tr>
                                <td>{cand['vaga']['titulo']}</td>
                                <td>{cand['vaga']['empresa']}</td>
                                <td>{cand['vaga']['plataforma']}</td>
                                <td>{cand['data_aplicacao']}</td>
                                <td class="status-{status}">{status.replace('_', ' ').title()}</td>
                                <td>{cand.get('ultima_atualizacao', cand['data_aplicacao'])}</td>
                                <td>
                                    <a href="{cand['vaga']['link']}" target="_blank">Ver Vaga</a>
                                </td>
                            </tr>
                    """
        
        html_dashboard += f"""
                        </tbody>
                    </table>
                </div>
                
                <button class="refresh-btn" onclick="location.reload()">
                    🔄 Atualizar Dashboard
                </button>
                
                <div style="margin-top: 30px; text-align: center;">
                    <p><strong>Portfolio:</strong> <a href="{self.config['portfolio']}" target="_blank">carloscostato-cmyk.github.io/Costato/</a></p>
                    <p><strong>LinkedIn:</strong> <a href="{self.config['linkedin']}" target="_blank">linkedin.com/in/carlos-costato/</a></p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Salvar dashboard
        with open('dashboard-feedback.html', 'w', encoding='utf-8') as f:
            f.write(html_dashboard)
        
        print("Dashboard gerado: dashboard-feedback.html")
    
    def executar_verificacao_feedback(self):
        """Executa verificação completa de feedback"""
        print("GERENTE DE PROJETOS - INICIANDO VERIFICACAO DE FEEDBACK")
        print("="*60)
        
        # Carregar candidaturas existentes
        candidaturas = self.carregar_candidaturas()
        print(f"Total de candidaturas ativas: {len(candidaturas)}")
        
        # Verificar todos os canais
        todas_respostas = []
        
        # 1. Verificar email
        respostas_email = self.verificar_email_respostas()
        todas_respostas.extend(respostas_email)
        
        # 2. Verificar LinkedIn
        respostas_linkedin = self.verificar_linkedin_mensagens()
        todas_respostas.extend(respostas_linkedin)
        
        # 3. Verificar WhatsApp
        respostas_whatsapp = self.verificar_whatsapp_mensagens()
        todas_respostas.extend(respostas_whatsapp)
        
        # 4. Atualizar status
        atualizacoes = self.atualizar_status_candidaturas(todas_respostas)
        
        if atualizacoes:
            print(f"\n{len(atualizacoes)} ATUALIZACOES ENCONTRADAS:")
            print("-"*60)
            
            for i, atualizacao in enumerate(atualizacoes, 1):
                print(f"\n{i}. {atualizacao['vaga']} - {atualizacao['empresa']}")
                print(f"   Status: {atualizacao['status_anterior']} -> {atualizacao['status_novo']}")
                print(f"   Data: {atualizacao['data']}")
                print(f"   Mensagem: {atualizacao['mensagem']}")
            
            # 5. Enviar notificações
            print(f"\nENVIANDO NOTIFICACOES...")
            self.enviar_notificacao_email(atualizacoes)
            self.enviar_notificacao_whatsapp(atualizacoes)
            
            # 6. Gerar dashboard
            print(f"\nGERANDO DASHBOARD...")
            self.gerar_dashboard_feedback()
            
            # 7. Gerar relatório
            relatorio = {
                'data_verificacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_candidaturas': len(candidaturas),
                'total_atualizacoes': len(atualizacoes),
                'canais_verificados': ['Email', 'LinkedIn', 'WhatsApp'],
                'atualizacoes': atualizacoes
            }
            
            with open('relatorio-feedback.json', 'w', encoding='utf-8') as f:
                json.dump(relatorio, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"\nRelatorio salvo: relatorio-feedback.json")
            print(f"Dashboard: dashboard-feedback.html")
            
        else:
            print(f"\nNenhuma atualizacao encontrada nesta verificacao")
            print(f"Tente novamente em algumas horas")
        
        print(f"\nVERIFICACAO CONCLUIDA!")
        print(f"Proxima verificacao em: 4 horas")
        
        return atualizacoes
    
    def agendar_verificacoes_automaticas(self):
        """Agenda verificações automáticas (simulação)"""
        print("AGENDANDO VERIFICACOES AUTOMATICAS...")
        
        # Simulação de agendamento
        agendamentos = [
            {"horario": "09:00", "status": "ativo"},
            {"horario": "13:00", "status": "ativo"},
            {"horario": "17:00", "status": "ativo"},
            {"horario": "21:00", "status": "ativo"}
        ]
        
        for ag in agendamentos:
            print(f"Verificacao agendada: {ag['horario']} - {ag['status']}")
        
        print(f"\nTotal de {len(agendamentos)} verificacoes diarias agendadas")
        print(f"Sistema verificara automaticamente a cada 4 horas")

# Executar verificação de feedback
if __name__ == "__main__":
    gerente = GerenteFeedbackVagas()
    gerente.executar_verificacao_feedback()
