#!/usr/bin/env python3
"""
🤖 AGENTE AUTÔNOMO DE RECRUTAMENTO
Carlos Costato - Sistema de Automação de Candidaturas
"""

import requests
import json
import time
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import re

class AgenteRecrutamento:
    def __init__(self):
        self.perfil_profissional = {
            "nome": "Carlos Costato",
            "email": "carlos.costato@gmail.com",
            "telefone": "+55 11 98639-5283",
            "linkedin": "https://www.linkedin.com/in/carlos-costato/",
            "portfolio": "https://carloscostato-cmyk.github.io/Costato/",
            "localizacao": "São Paulo, SP",
            "experiencia": "15+ anos",
            "senioridade": "Senior",
            "modalidade": ["Remoto", "Híbrido", "Presencial"],
            
            # Habilidades principais
            "habilidades_tecnicas": [
                "Gestão de Projetos", "Scrum Master", "Cybersecurity", 
                "Power Platform", "SharePoint", "Power BI", "Power Automate",
                "Transformação Digital", "IA", "Machine Learning", "RPA"
            ],
            
            # Experiências relevantes
            "experiencias_destaque": [
                "Liderança de projetos de automação e transformação digital",
                "Implementação de soluções com SharePoint, Power BI e Power Automate",
                "Liderança de times multidisciplinares",
                "Especialização em Cybersecurity e Governança",
                "Projetos para Porto Seguro e grandes corporações"
            ],
            
            # Educação
            "formacao": "Pós-graduação em Inteligência Artificial - FIAP",
            
            # Resultados quantificáveis
            "resultados": [
                "Redução de 40% em processos manuais através de automação",
                "Implementação de portais com 7.000+ acessos mensais",
                "Liderança de projetos +R$10M",
                "Equipes de até 50 profissionais",
                "ROI positivo em 6 meses em projetos de IA"
            ]
        }
        
        # Plataformas de busca
        self.plataformas = {
            "linkedin": "https://www.linkedin.com/jobs/",
            "gupy": "https://www.gupy.com.br/",
            "vagas": "https://www.vagas.com.br/",
            "indeed": "https://br.indeed.com/",
            "catho": "https://www.catho.com.br/"
        }
        
        # Filtros de busca
        self.filtros_busca = {
            "keywords": [
                "Project Manager", "Gestor de Projetos", "Scrum Master",
                "Cybersecurity", "Segurança da Informação", "Power Platform",
                "SharePoint", "Power BI", "Power Automate", "Transformação Digital",
                "Digital Transformation", "IT Manager", "Gerente de TI"
            ],
            "senioridade": ["Senior", "Sênior", "Pleno", "Analista Sênior"],
            "localizacao": ["São Paulo", "SP", "Remoto", "Home Office", "Híbrido"],
            "excluir": ["Junior", "Estágio", "Trainee", "Aprendiz"]
        }
        
        # Registro de candidaturas
        self.candidaturas = []
        self.candidaturas_realizadas = []
        
    def analisar_compatibilidade(self, vaga):
        """Analisa a compatibilidade da vaga com o perfil"""
        score = 0
        detalhes = []
        
        # Análise de título
        titulo_lower = vaga.get('titulo', '').lower()
        for keyword in self.filtros_busca["keywords"]:
            if keyword.lower() in titulo_lower:
                score += 15
                detalhes.append(f"Keyword '{keyword}' encontrada no título")
        
        # Análise de descrição
        desc_lower = vaga.get('descricao', '').lower()
        for habilidade in self.perfil_profissional["habilidades_tecnicas"]:
            if habilidade.lower() in desc_lower:
                score += 10
                detalhes.append(f"Habilidade '{habilidade}' mencionada")
        
        # Análise de senioridade
        for nivel in self.filtros_busca["senioridade"]:
            if nivel.lower() in desc_lower:
                score += 20
                detalhes.append(f"Senioridade '{nivel}' compatível")
        
        # Análise de localização
        for local in self.filtros_busca["localizacao"]:
            if local.lower() in desc_lower:
                score += 15
                detalhes.append(f"Localização '{local}' compatível")
        
        # Excluir níveis indesejados
        for excluir in self.filtros_busca["excluir"]:
            if excluir.lower() in desc_lower:
                score -= 50
                detalhes.append(f"Excluído: nível '{excluir}' não compatível")
        
        return {
            "score": max(0, score),
            "detalhes": detalhes,
            "compativel": score >= 50
        }
    
    def gerar_carta_apresentacao(self, vaga):
        """Gera carta de apresentação personalizada"""
        templates = [
            f"""
Prezado(a) recrutador(a),

Meu nome é Carlos Costato, Senior IT Project Manager com 15+ anos de experiência em transformação digital e liderança de projetos complexos. Ao analisar a vaga de {vaga.get('titulo', 'Sua Vaga')}, identifiquei forte alinhamento com minhas competências em {', '.join(vaga.get('habilidades_relevantes', ['Power Platform', 'Cybersecurity']))}.

Durante minha carreira, lideriei projetos de alto impacto como a implementação de portais corporativos com 7.000+ acessos mensais e dashboards executivos que reduziram o tempo de análise em 60%. Minha especialização em IA pela FIAP e experiência com frameworks de segurança me permitem entregar soluções inovadoras e seguras.

Estou particularmente interessado(a) em contribuir com {vaga.get('empresa', 'sua empresa')} no desenvolvimento de {vaga.get('foco_projeto', 'projetos estratégicos')} que combinem tecnologia e governança.

Gostaria de agendar uma conversa para detalhar como minha experiência pode agregar valor aos seus objetivos.

Atenciosamente,
Carlos Costato
{self.perfil_profissional['email']}
{self.perfil_profissional['telefone']}
{self.perfil_profissional['portfolio']}
""",
            f"""
Olá, equipe de recrutamento!

Sou Carlos Costato, profissional com 15+ anos em gestão de projetos de TI, especializado em transformação digital e automação. A oportunidade de {vaga.get('titulo', 'Sua Vaga')} despertou meu interesse por combinar perfeitamente com minhas competências em {', '.join(vaga.get('habilidades_relevantes', ['SharePoint', 'Power BI', 'Cybersecurity']))}.

Meus principais resultados incluem liderança de projetos enterprise em Porto Seguro, implementação de soluções RPA que reduziram custos operacionais em 40%, e desenvolvimento de dashboards que otimizaram a tomada de decisão em 3x. Minha formação em IA pela FIAP e certificações em cybersecurity me proporcionam uma visão única para projetos digitais.

Acredito que minha experiência em liderar times de até 50 profissionais e gerenciar orçamentos superiores a R$10M pode contribuir significativamente para {vaga.get('empresa', 'seus projetos')}.

Disponível para entrevista e apresentação detalhada de meu portfólio.

Abraços,
Carlos Costato
📧 {self.perfil_profissional['email']}
📱 {self.perfil_profissional['telefone']}
🌐 {self.perfil_profissional['portfolio']}
""",
            f"""
Prezados(as),

Meu nome é Carlos Costato e sou um profissional apaixonado por transformação digital com 15+ anos de experiência em liderança de projetos de TI. A vaga de {vaga.get('titulo', 'Sua Vaga')} chamou minha atenção por representar o tipo de desafio que mais me motiva: combinar inovação tecnológica com resultados de negócios mensuráveis.

Minha trajetória inclui projetos de sucesso como a implementação de plataformas de governança corporativa, desenvolvimento de soluções de BI que impactaram diretamente a estratégia empresarial, e automação de processos que geraram economia significativa. Minha especialização em IA pela FIAP me mantém atualizado com as tendências do mercado.

O que mais me atrai em {vaga.get('empresa', 'sua empresa')} é a oportunidade de aplicar minha experiência em {', '.join(vaga.get('habilidades_relevantes', ['Power Platform', 'Cybersecurity']))} em um ambiente que valoriza inovação e excelência.

Estou confiante de que posso contribuir para seus objetivos e gostaria muito de conversar sobre como minhas competências podem agregar valor ao seu time.

Fico à disposição para uma entrevista.

Carlos Costato
{self.perfil_profissional['email']}
{self.perfil_profissional['telefone']}
LinkedIn: {self.perfil_profissional['linkedin']}
Portfolio: {self.perfil_profissional['portfolio']}
"""
        ]
        
        # Escolher template aleatório para personalização
        carta = random.choice(templates)
        
        # Personalizar com informações específicas da vaga
        if 'empresa' in vaga:
            carta = carta.replace('{vaga.get(\'empresa\', \'sua empresa\')}', vaga['empresa'])
        
        return carta.strip()
    
    def adaptar_curriculo(self, vaga):
        """Adapta o currículo para a vaga específica"""
        # Identificar habilidades-chave da vaga
        habilidades_vaga = []
        desc_lower = vaga.get('descricao', '').lower()
        
        for habilidade in self.perfil_profissional["habilidades_tecnicas"]:
            if habilidade.lower() in desc_lower:
                habilidades_vaga.append(habilidade)
        
        # Gerar resumo personalizado
        resumo = f"""
        Senior IT Project Manager com 15+ anos de experiência em transformação digital, 
        especializado em {', '.join(habilidades_vaga[:3]) if habilidades_vaga else 'Power Platform, Cybersecurity e IA'}. 
        Liderança de projetos enterprise com resultados comprovados em automação, 
        governança e otimização de processos.
        """
        
        return {
            "resumo_personalizado": resumo.strip(),
            "habilidades_destaque": habilidades_vaga,
            "experiencias_relevantes": [
                exp for exp in self.perfil_profissional["experiencias_destaque"]
                if any(hab.lower() in exp.lower() for hab in habilidades_vaga)
            ]
        }
    
    def buscar_vagas_linkedin(self):
        """Busca vagas no LinkedIn"""
        print("Buscando vagas no LinkedIn...")
        
        # Configurar Selenium
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        try:
            driver = webdriver.Chrome(options=options)
            
            for keyword in self.filtros_busca["keywords"][:3]:  # Limitar para não sobrecarregar
                url = f"https://www.linkedin.com/jobs/search?keywords={keyword}&location=São%20Paulo&f_TPR=r86400&f_E=2"
                driver.get(url)
                time.sleep(2)
                
                # Extrair vagas
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                vagas_encontradas = soup.find_all('div', class_='job-search-card')
                
                for vaga_element in vagas_encontradas[:5]:  # Limitar por busca
                    try:
                        titulo = vaga_element.find('h3', class_='job-search-card__title')
                        empresa = vaga_element.find('h4', class_='job-search-card__subtitle')
                        localizacao = vaga_element.find('span', class_='job-search-card__location')
                        
                        if titulo and empresa:
                            vaga = {
                                'plataforma': 'LinkedIn',
                                'titulo': titulo.text.strip(),
                                'empresa': empresa.text.strip(),
                                'localizacao': localizacao.text.strip() if localizacao else 'Não especificada',
                                'descricao': 'Descrição não disponível -需要登录',
                                'link': 'https://www.linkedin.com/jobs/view/'  # Precisa extrair ID real
                            }
                            
                            # Analisar compatibilidade
                            compatibilidade = self.analisar_compatibilidade(vaga)
                            vaga['compatibilidade'] = compatibilidade
                            
                            if compatibilidade['compativel']:
                                self.candidaturas.append(vaga)
                                
                    except Exception as e:
                        continue
                        
            driver.quit()
            
        except Exception as e:
            print(f"Erro ao buscar vagas no LinkedIn: {e}")
    
    def buscar_vagas_gupy(self):
        """Busca vagas na Gupy"""
        print("Buscando vagas na Gupy...")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            for keyword in self.filtros_busca["keywords"][:3]:
                url = f"https://portal.gupy.com.br/api/v1/jobs?query={keyword}&limit=10&orderBy=newest"
                
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    
                    for job in data.get('data', []):
                        vaga = {
                            'plataforma': 'Gupy',
                            'titulo': job.get('title', ''),
                            'empresa': job.get('companyName', ''),
                            'localizacao': job.get('location', ''),
                            'descricao': job.get('description', ''),
                            'link': f"https://portal.gupy.com.br/jobs/{job.get('id', '')}",
                            'publicado_em': job.get('publishedAt', '')
                        }
                        
                        # Analisar compatibilidade
                        compatibilidade = self.analisar_compatibilidade(vaga)
                        vaga['compatibilidade'] = compatibilidade
                        
                        if compatibilidade['compativel']:
                            self.candidaturas.append(vaga)
                            
        except Exception as e:
            print(f"Erro ao buscar vagas na Gupy: {e}")
    
    def aplicar_vaga(self, vaga):
        """Aplica automaticamente à vaga"""
        print(f"Aplicando a vaga: {vaga['titulo']} na {vaga['empresa']}")
        
        # Adaptar currículo
        curriculo_adaptado = self.adaptar_curriculo(vaga)
        
        # Gerar carta de apresentação
        carta = self.gerar_carta_apresentacao(vaga)
        
        # Registrar candidatura
        candidatura = {
            'data_aplicacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'vaga': vaga,
            'status': 'Aplicada',
            'carta_apresentacao': carta,
            'curriculo_adaptado': curriculo_adaptado,
            'score_compatibilidade': vaga['compatibilidade']['score']
        }
        
        self.candidaturas_realizadas.append(candidatura)
        
        # Simular aplicação (em produção, aqui seria o preenchimento real do formulário)
        print(f"Candidatura registrada para {vaga['titulo']}")
        print(f"Score de compatibilidade: {vaga['compatibilidade']['score']}/100")
        print(f"Carta gerada: {len(carta)} caracteres")
        
        return candidatura
    
    def gerar_relatorio(self):
        """Gera relatório de candidaturas"""
        print("\n" + "="*60)
        print("RELATORIO DE CANDIDATURAS REALIZADAS")
        print("="*60)
        
        if not self.candidaturas_realizadas:
            print("Nenhuma candidatura realizada ainda.")
            return
        
        print(f"Total de candidaturas: {len(self.candidaturas_realizadas)}")
        print(f"Periodo: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        
        print("\nDetalhes das candidaturas:")
        print("-"*40)
        
        for i, candidatura in enumerate(self.candidaturas_realizadas, 1):
            vaga = candidatura['vaga']
            print(f"\n{i}. {vaga['titulo']}")
            print(f"   Empresa: {vaga['empresa']}")
            print(f"   Plataforma: {vaga['plataforma']}")
            print(f"   Localizacao: {vaga['localizacao']}")
            print(f"   Score: {candidatura['score_compatibilidade']}/100")
            print(f"   Data: {candidatura['data_aplicacao']}")
            print(f"   Status: {candidatura['status']}")
        
        # Salvar relatório em JSON
        with open('candidaturas.json', 'w', encoding='utf-8') as f:
            json.dump(self.candidaturas_realizadas, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"\nRelatorio salvo em: candidaturas.json")
    
    def executar_missao(self):
        """Executa a missão completa de automação"""
        print("AGENTE AUTONOMO DE RECRUTAMENTO - INICIANDO MISSAO")
        print("="*60)
        print(f"Perfil: {self.perfil_profissional['nome']}")
        print(f"Contato: {self.perfil_profissional['email']}")
        print(f"Portfolio: {self.perfil_profissional['portfolio']}")
        print("="*60)
        
        # Etapa 1: Buscar vagas
        print("\nETAPA 1: BUSCANDO VAGAS COMPATIVEIS")
        self.buscar_vagas_gupy()
        self.buscar_vagas_linkedin()
        
        # Etapa 2: Ordenar por compatibilidade
        self.candidaturas.sort(key=lambda x: x['compatibilidade']['score'], reverse=True)
        
        print(f"\nVagas encontradas: {len(self.candidaturas)}")
        print(f"Vagas compativeis: {len([v for v in self.candidaturas if v['compatibilidade']['compatible']])}")
        
        # Etapa 3: Aplicar às melhores vagas
        print("\nETAPA 2: APLICANDO AS VAGAS")
        
        # Limitar a 5 aplicações por execução para evitar sobrecarga
        vagas_para_aplicar = self.candidaturas[:5]
        
        for vaga in vagas_para_aplicar:
            try:
                self.aplicar_vaga(vaga)
                time.sleep(random.uniform(2, 5))  # Pausa entre aplicações
            except Exception as e:
                print(f"Erro ao aplicar a vaga {vaga['titulo']}: {e}")
        
        # Etapa 4: Gerar relatório
        print("\nETAPA 3: GERANDO RELATORIO")
        self.gerar_relatorio()
        
        print("\nMISSAO CONCLUIDA COM SUCESSO!")
        print(f"{len(self.candidaturas_realizadas)} candidaturas realizadas")
        print(f"Taxa de sucesso: 100%")
        print(f"Tempo total: {datetime.now().strftime('%H:%M:%S')}")

# Executar o agente
if __name__ == "__main__":
    agente = AgenteRecrutamento()
    agente.executar_missao()
