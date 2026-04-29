#!/usr/bin/env python3
"""
🤖 DEMO - Sistema de Recrutamento com Vagas Simuladas
Demonstração do funcionamento do agente com dados de teste
"""

import json
from datetime import datetime
import random

class DemoRecrutamento:
    def __init__(self):
        # Vagas de teste realistas para o perfil de Carlos Costato
        self.vagas_demo = [
            {
                "plataforma": "LinkedIn",
                "titulo": "Senior IT Project Manager",
                "empresa": "Tech Solutions Brasil",
                "localizacao": "São Paulo, SP",
                "descricao": """
                Buscamos um Senior IT Project Manager com experiência em transformação digital e liderança de projetos complexos. 
                Requisitos: experiência com Power Platform, SharePoint, e cybersecurity. 
                Responsável por gerenciar projetos de até R$10M e equipes de 20+ pessoas.
                Modalidade: Híbrido (3 dias na empresa, 2 dias remoto).
                Salário: R$15.000 - R$20.000.
                """,
                "link": "https://linkedin.com/jobs/view/123456",
                "publicado_em": "2024-04-27"
            },
            {
                "plataforma": "Gupy",
                "titulo": "Scrum Master Senior",
                "empresa": "Digital Innovation Hub",
                "localizacao": "Remoto",
                "descricao": """
                Procuramos Scrum Master Senior com experiência em metodologias ágeis e gestão de projetos de TI.
                Conhecimento em Power BI, automação de processos e cybersecurity é um diferencial.
                O candidato irá liderar times de desenvolvimento e projetos de transformação digital.
                Experiência mínima de 5 anos em cargos de liderança.
                Contratação CLT, benefícios completos.
                """,
                "link": "https://portal.gupy.com.br/jobs/789012",
                "publicado_em": "2024-04-26"
            },
            {
                "plataforma": "Vagas.com.br",
                "titulo": "Gerente de Projetos de TI",
                "empresa": "Financial Services Corp",
                "localizacao": "São Paulo, SP",
                "descricao": """
                Gerente de Projetos de TI para área de serviços financeiros. 
                Experiência com SharePoint, Power BI e implementação de soluções de cybersecurity.
                Responsável por projetos de governança e compliance digital.
                Experiência com frameworks de gestão (PMBOK, Agile) é essencial.
                Salário competitivo + bônus por performance.
                """,
                "link": "https://www.vagas.com.br/vagas/345678",
                "publicado_em": "2024-04-25"
            },
            {
                "plataforma": "Indeed",
                "titulo": "IT Project Manager - Cybersecurity",
                "empresa": "SecureTech Solutions",
                "localizacao": "Remoto",
                "descricao": """
                IT Project Manager especializado em projetos de cybersecurity e governança digital.
                Experiência com implementação de frameworks de segurança, Power Platform e automação.
                Liderança de equipes multidisciplinares e gestão de stakeholders.
                Certificações em cybersecurity (CISSP, CISM) são valorizadas.
                Ambiente remoto com flexibilidade de horários.
                """,
                "link": "https://br.indeed.com/jobs/901234",
                "publicado_em": "2024-04-24"
            },
            {
                "plataforma": "Catho",
                "titulo": "Product Owner - Power Platform",
                "empresa": "Cloud Systems Integration",
                "localizacao": "Híbrido - São Paulo",
                "descricao": """
                Product Owner com experiência em Power Platform (Power BI, Power Apps, Power Automate).
                Responsável pelo backlog de produtos digitais e alinhamento com estratégia de negócios.
                Experiência com metodologias ágeis e gestão de expectativas de stakeholders.
                Conhecimento em SharePoint e automação de processos é necessário.
                Oportunidade de crescimento em empresa de tecnologia em expansão.
                """,
                "link": "https://www.catho.com.br/vagas/567890",
                "publicado_em": "2024-04-23"
            },
            {
                "plataforma": "LinkedIn",
                "titulo": "Digital Transformation Manager",
                "empresa": "Enterprise Digital Solutions",
                "localizacao": "São Paulo, SP",
                "descricao": """
                Digital Transformation Manager para liderar projetos de transformação digital em grande empresa.
                Experiência com Power Platform, SharePoint, IA e automação de processos.
                Gestão de portfólio de projetos com orçamentos superiores a R$5M.
                Liderança de equipes de até 30 pessoas e coordenação de fornecedores.
                Inglês fluente e experiência com metodologias ágeis.
                """,
                "link": "https://linkedin.com/jobs/view/234567",
                "publicado_em": "2024-04-22"
            },
            {
                "plataforma": "Gupy",
                "titulo": "Program Manager - IA & Automation",
                "empresa": "AI Innovation Labs",
                "localizacao": "Remoto",
                "descricao": """
                Program Manager para projetos de Inteligência Artificial e automação inteligente.
                Experiência com implementação de soluções de IA, machine learning e RPA.
                Gestão de programas complexos com múltiplos projetos interdependentes.
                Conhecimento em Power BI, cybersecurity e governança de dados.
                Formação em áreas de tecnologia é um diferencial.
                """,
                "link": "https://portal.gupy.com.br/jobs/345678",
                "publicado_em": "2024-04-21"
            },
            {
                "plataforma": "Vagas.com.br",
                "titulo": "IT Governance Manager",
                "empresa": "Compliance & Risk Management",
                "localizacao": "São Paulo, SP",
                "descricao": """
                IT Governance Manager para implementação de frameworks de governança e compliance.
                Experiência com cybersecurity, GDPR, LGPD e padrões internacionais.
                Gestão de projetos de auditoria e conformidade digital.
                Conhecimento em SharePoint para gestão documental e Power BI para dashboards.
                Certificações COBIT, ITIL ou similares são valorizadas.
                """,
                "link": "https://www.vagas.com.br/vagas/123789",
                "publicado_em": "2024-04-20"
            }
        ]
        
        # Perfil profissional
        self.perfil_profissional = {
            "nome": "Carlos Costato",
            "email": "carlos.costato@gmail.com",
            "telefone": "+55 11 98639-5283",
            "linkedin": "https://www.linkedin.com/in/carlos-costato/",
            "portfolio": "https://carloscostato-cmyk.github.io/Costato/",
            "experiencia": "15+ anos",
            "habilidades": [
                "Gestão de Projetos", "Scrum Master", "Cybersecurity", 
                "Power Platform", "SharePoint", "Power BI", "Power Automate",
                "Transformação Digital", "IA", "Machine Learning", "RPA"
            ]
        }
    
    def analisar_compatibilidade(self, vaga):
        """Analisa a compatibilidade da vaga com o perfil"""
        score = 0
        detalhes = []
        
        # Análise de título
        titulo_lower = vaga['titulo'].lower()
        keywords_titulo = ["project manager", "scrum master", "product owner", "program manager", "gerente", "manager"]
        
        for keyword in keywords_titulo:
            if keyword in titulo_lower:
                score += 25
                detalhes.append(f"Keyword '{keyword}' encontrada no título")
                break
        
        # Análise de descrição
        desc_lower = vaga['descricao'].lower()
        
        # Habilidades principais
        habilidades_principais = ["power platform", "sharepoint", "power bi", "cybersecurity", "transformação digital"]
        for habilidade in habilidades_principais:
            if habilidade in desc_lower:
                score += 15
                detalhes.append(f"Habilidade '{habilidade}' mencionada")
        
        # Nível de senioridade
        senioridade_keywords = ["senior", "sênior", "pleno", "experiência"]
        for nivel in senioridade_keywords:
            if nivel in desc_lower:
                score += 20
                detalhes.append(f"Senioridade compatível")
                break
        
        # Localização
        local_keywords = ["são paulo", "sp", "remoto", "home office", "híbrido"]
        for local in local_keywords:
            if local in desc_lower:
                score += 15
                detalhes.append(f"Localização compatível")
                break
        
        # Excluir níveis junior
        excluir_keywords = ["junior", "estágio", "trainee"]
        for excluir in excluir_keywords:
            if excluir in desc_lower:
                score -= 50
                detalhes.append(f"Excluído: nível não compatível")
                break
        
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

Meu nome é Carlos Costato, Senior IT Project Manager com 15+ anos de experiência em transformação digital e liderança de projetos complexos. Ao analisar a vaga de {vaga['titulo']}, identifiquei forte alinhamento com minhas competências em gestão de projetos enterprise e implementação de soluções tecnológicas inovadoras.

Durante minha carreira, lideriei projetos de alto impacto como a implementação de portais corporativos com 7.000+ acessos mensais e dashboards executivos que reduziram o tempo de análise em 60%. Minha especialização em IA pela FIAP e experiência com frameworks de segurança me permitem entregar soluções inovadoras e seguras.

Estou particularmente interessado(a) em contribuir com {vaga['empresa']} no desenvolvimento de projetos estratégicos que combinem tecnologia e governança corporativa.

Gostaria de agendar uma conversa para detalhar como minha experiência pode agregar valor aos seus objetivos.

Atenciosamente,
Carlos Costato
{self.perfil_profissional['email']}
{self.perfil_profissional['telefone']}
{self.perfil_profissional['portfolio']}
""",
            f"""
Olá, equipe de recrutamento!

Sou Carlos Costato, profissional com 15+ anos em gestão de projetos de TI, especializado em transformação digital e automação. A oportunidade de {vaga['titulo']} despertou meu interesse por combinar perfeitamente com minhas competências em liderança de projetos complexos e implementação de soluções enterprise.

Meus principais resultados incluem liderança de projetos em Porto Seguro, implementação de soluções que reduziram custos operacionais em 40%, e desenvolvimento de dashboards que otimizaram a tomada de decisão em 3x. Minha formação em IA pela FIAP e certificações em cybersecurity me proporcionam uma visão única para projetos digitais.

Acredito que minha experiência em liderar times de até 50 profissionais e gerenciar orçamentos superiores a R$10M pode contribuir significativamente para {vaga['empresa']}.

Disponível para entrevista e apresentação detalhada de meu portfólio.

Abraços,
Carlos Costato
📧 {self.perfil_profissional['email']}
📱 {self.perfil_profissional['telefone']}
🌐 {self.perfil_profissional['portfolio']}
""",
            f"""
Prezados(as),

Meu nome é Carlos Costato e sou um profissional apaixonado por transformação digital com 15+ anos de experiência em liderança de projetos de TI. A vaga de {vaga['titulo']} chamou minha atenção por representar o tipo de desafio que mais me motiva: combinar inovação tecnológica com resultados de negócios mensuráveis.

Minha trajetória inclui projetos de sucesso como a implementação de plataformas de governança corporativa, desenvolvimento de soluções de BI que impactaram diretamente a estratégia empresarial, e automação de processos que geraram economia significativa. Minha especialização em IA pela FIAP me mantém atualizado com as tendências do mercado.

O que mais me atrai em {vaga['empresa']} é a oportunidade de aplicar minha experiência em projetos estratégicos que unem tecnologia, governança e inovação.

Estou confiante de que posso contribuir para seus objetivos e gostaria muito de conversar sobre como minhas competências podem agregar valor ao seu time.

Fico à disposição para uma entrevista.

Carlos Costato
{self.perfil_profissional['email']}
{self.perfil_profissional['telefone']}
LinkedIn: {self.perfil_profissional['linkedin']}
Portfolio: {self.perfil_profissional['portfolio']}
"""
        ]
        
        # Escolher template aleatório
        carta = random.choice(templates)
        return carta.strip()
    
    def adaptar_curriculo(self, vaga):
        """Adapta o currículo para a vaga específica"""
        desc_lower = vaga['descricao'].lower()
        
        # Identificar habilidades-chave da vaga
        habilidades_vaga = []
        habilidades_map = {
            "power platform": "Power Platform",
            "sharepoint": "SharePoint", 
            "power bi": "Power BI",
            "power automate": "Power Automate",
            "cybersecurity": "Cybersecurity",
            "transformação digital": "Transformação Digital",
            "ia": "Inteligência Artificial",
            "machine learning": "Machine Learning",
            "rpa": "RPA",
            "scrum": "Scrum",
            "agile": "Agile"
        }
        
        for key, value in habilidades_map.items():
            if key in desc_lower:
                habilidades_vaga.append(value)
        
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
                "Liderança de projetos de automação e transformação digital",
                "Implementação de soluções com SharePoint, Power BI e Power Automate", 
                "Liderança de times multidisciplinares",
                "Especialização em Cybersecurity e Governança",
                "Projetos para Porto Seguro e grandes corporações"
            ]
        }
    
    def aplicar_vaga(self, vaga):
        """Aplica automaticamente à vaga"""
        print(f"Aplicando a vaga: {vaga['titulo']} na {vaga['empresa']}")
        
        # Analisar compatibilidade
        compatibilidade = self.analisar_compatibilidade(vaga)
        
        if not compatibilidade['compativel']:
            print(f"Vaga incompatível (score: {compatibilidade['score']})")
            return None
        
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
            'score_compatibilidade': compatibilidade['score'],
            'compatibilidade_detalhes': compatibilidade['detalhes']
        }
        
        print(f"Candidatura registrada - Score: {compatibilidade['score']}/100")
        print(f"Carta gerada: {len(carta)} caracteres")
        
        return candidatura
    
    def executar_demo(self):
        """Executa a demonstração completa"""
        print("AGENTE AUTONOMO DE RECRUTAMENTO - DEMO COM VAGAS REAIS")
        print("="*70)
        print(f"Perfil: {self.perfil_profissional['nome']}")
        print(f"Experiência: {self.perfil_profissional['experiencia']}")
        print(f"Portfolio: {self.perfil_profissional['portfolio']}")
        print("="*70)
        
        print(f"\nANALISANDO {len(self.vagas_demo)} VAGAS DISPONÍVEIS...")
        print("-"*70)
        
        candidaturas_realizadas = []
        
        # Analisar cada vaga
        for i, vaga in enumerate(self.vagas_demo, 1):
            print(f"\n{i}. Analisando: {vaga['titulo']} - {vaga['empresa']}")
            print(f"   Plataforma: {vaga['plataforma']}")
            print(f"   Localização: {vaga['localizacao']}")
            
            candidatura = self.aplicar_vaga(vaga)
            if candidatura:
                candidaturas_realizadas.append(candidatura)
                print(f"   COMPATIVEL - Score: {candidatura['score_compatibilidade']}/100")
            else:
                print(f"   INCOMPATIVEL")
        
        # Gerar relatório final
        print("\n" + "="*70)
        print("RELATÓRIO FINAL DA DEMO")
        print("="*70)
        
        print(f"\nTotal de vagas analisadas: {len(self.vagas_demo)}")
        print(f"Vagas compatíveis: {len(candidaturas_realizadas)}")
        print(f"Taxa de compatibilidade: {len(candidaturas_realizadas)/len(self.vagas_demo)*100:.1f}%")
        
        if candidaturas_realizadas:
            print(f"\nTOP 3 VAGAS MAIS COMPATIVEIS:")
            print("-"*70)
            
            # Ordenar por score
            candidaturas_ordenadas = sorted(candidaturas_realizadas, 
                                        key=lambda x: x['score_compatibilidade'], 
                                        reverse=True)
            
            for i, candidatura in enumerate(candidaturas_ordenadas[:3], 1):
                vaga = candidatura['vaga']
                print(f"\n{i}. {vaga['titulo']}")
                print(f"   Empresa: {vaga['empresa']}")
                print(f"   Plataforma: {vaga['plataforma']}")
                print(f"   Score: {candidatura['score_compatibilidade']}/100")
                print(f"   Localizacao: {vaga['localizacao']}")
                print(f"   Link: {vaga['link']}")
        
        # Salvar relatório em JSON
        relatorio_demo = {
            'data_execucao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'perfil': self.perfil_profissional,
            'estatisticas': {
                'total_vagas_analisadas': len(self.vagas_demo),
                'vagas_compativeis': len(candidaturas_realizadas),
                'taxa_compatibilidade': len(candidaturas_realizadas)/len(self.vagas_demo)*100,
                'score_medio': sum(c['score_compatibilidade'] for c in candidaturas_realizadas)/len(candidaturas_realizadas) if candidaturas_realizadas else 0
            },
            'candidaturas': candidaturas_realizadas
        }
        
        with open('demo-candidaturas.json', 'w', encoding='utf-8') as f:
            json.dump(relatorio_demo, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"\nRelatorio salvo em: demo-candidaturas.json")
        print(f"\nDEMO CONCLUIDA COM SUCESSO!")
        print(f"{len(candidaturas_realizadas)} candidaturas prontas para envio!")
        print(f"Taxa de sucesso: {len(candidaturas_realizadas)/len(self.vagas_demo)*100:.1f}%")

# Executar a demonstração
if __name__ == "__main__":
    demo = DemoRecrutamento()
    demo.executar_demo()
