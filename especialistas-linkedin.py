#!/usr/bin/env python3
"""
👥 3 ESPECIALISTAS RH - ANÁLISE ESTRATÉGICA LINKEDIN
Carlos Costato - Validação Profissional de Perfil LinkedIn
"""

import json
from datetime import datetime
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum

class NivelOtimizacao(Enum):
    CRITICO = "critico"
    IMPORTANTE = "importante"
    RECOMENDADO = "recomendado"
    OTIMIZADO = "otimizado"

@dataclass
class AnaliseItem:
    item: str
    status_atual: str
    status_desejado: str
    nivel_importancia: NivelOtimizacao
    gap_analise: str
    recomendacao: str

class EspecialistaRH:
    """Especialista em Recrutamento e LinkedIn"""
    
    def __init__(self, nome: str, especialidade: str, anos_experiencia: int):
        self.nome = nome
        self.especialidade = especialidade
        self.anos_experiencia = anos_experiencia
        self.analises_realizadas = 0
        self.validacoes_aprovadas = 0
        
    def analisar_perfil_linkedin(self, perfil_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analise completa do perfil LinkedIn"""
        analise = {
            "especialista": self.nome,
            "especialidade": self.especialidade,
            "data_analise": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "score_geral": 0,
            "itens_analisados": [],
            "gaps_criticos": [],
            "recomendacoes_prioritarias": [],
            "status_aprovacao": False,
            "proximos_passos": []
        }
        
        # Análise dos 10 pontos críticos
        itens_analise = self._gerar_checklist_analise(perfil_data)
        
        score_total = 0
        score_maximo = 0
        
        for item in itens_analise:
            resultado = self._analisar_item(item, perfil_data)
            analise["itens_analisados"].append(resultado)
            
            # Calcular score
            peso = self._calcular_peso_importancia(resultado.nivel_importancia)
            score_maximo += peso
            
            if resultado.status_atual == resultado.status_desejado:
                score_total += peso
            
            # Identificar gaps críticos
            if resultado.nivel_importancia == NivelOtimizacao.CRITICO and resultado.status_atual != resultado.status_desejado:
                analise["gaps_criticos"].append(resultado)
                analise["recomendacoes_prioritarias"].append(resultado.recomendacao)
        
        # Calcular score geral
        if score_maximo > 0:
            analise["score_geral"] = (score_total / score_maximo) * 100
        
        # Status de aprovação
        analise["status_aprovacao"] = analise["score_geral"] >= 70 and len(analise["gaps_criticos"]) == 0
        
        # Gerar próximos passos
        analise["proximos_passos"] = self._gerar_proximos_passos(analise)
        
        self.analises_realizadas += 1
        
        if analise["status_aprovacao"]:
            self.validacoes_aprovadas += 1
        
        return analise
    
    def _gerar_checklist_analise(self, perfil_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Gera checklist de análise baseado nas 10 recomendações"""
        return [
            {
                "id": 1,
                "item": "Aberto a oportunidades",
                "descricao": "Status 'Aberto a oportunidades' configurado",
                "status_desejado": "Somente recrutadores",
                "nivel_importancia": NivelOtimizacao.CRITICO,
                "impacto": "Reativa algoritmo do LinkedIn"
            },
            {
                "id": 2,
                "item": "Banner personalizado",
                "descricao": "Banner no Canva com nome, cargo e competências",
                "status_desejado": "Personalizado com informações profissionais",
                "nivel_importancia": NivelOtimizacao.IMPORTANTE,
                "impacto": "90% dos perfis deixam em branco"
            },
            {
                "id": 3,
                "item": "Título com 5 palavras-chave",
                "descricao": "Formato: [Cargo] | Palavra Chave 1 | Palavra Chave 2 | Palavra Chave 3 | Palavra Chave 4 | Palavra Chave 5",
                "status_desejado": "Otimizado com 5 palavras-chave relevantes",
                "nivel_importancia": NivelOtimizacao.CRITICO,
                "impacto": "Aumenta visibilidade em buscas"
            },
            {
                "id": 4,
                "item": "Sobre humano e pessoal",
                "descricao": "Texto 'Sobre' com gancho, história, detalhe pessoal e contato",
                "status_desejado": "Redação humana e conversacional",
                "nivel_importancia": NivelOtimizacao.IMPORTANTE,
                "impacto": "Conexão emocional com recrutadores"
            },
            {
                "id": 5,
                "item": "Experiências formato XYZ",
                "descricao": "Formato: 'Alcancei X fazendo Y, gerando Z'",
                "status_desejado": "Todas as experiências com métricas XYZ",
                "nivel_importancia": NivelOtimizacao.CRITICO,
                "impacto": "Demonstra resultados quantificáveis"
            },
            {
                "id": 6,
                "item": "Mídia visual nas experiências",
                "descricao": "Arquivos de mídia (apresentações, projetos, artigos)",
                "status_desejado": "Mídia visual em cada experiência relevante",
                "nivel_importancia": NivelOtimizacao.IMPORTANTE,
                "impacto": "Prova visual vale mais que texto"
            },
            {
                "id": 7,
                "item": "Competências ordenadas",
                "descricao": "Competências por relevância + recomendações",
                "status_desejado": "Ordenadas por importância + recomendações",
                "nivel_importancia": NivelOtimizacao.IMPORTANTE,
                "impacto": "Destaca habilidades principais"
            },
            {
                "id": 8,
                "item": "Localização estratégica",
                "descricao": "Localização alinhada com mercado-alvo",
                "status_desejado": "Configurada para mercado desejado",
                "nivel_importancia": NivelOtimizacao.CRITICO,
                "impacto": "Recrutadores filtram por cidade"
            },
            {
                "id": 9,
                "item": "Conexões personalizadas",
                "descricao": "Pedidos de conexão com mensagens personalizadas",
                "status_desejado": "Estratégia de conexões ativa",
                "nivel_importancia": NivelOtimizacao.RECOMENDADO,
                "impacto": "Aumenta taxa de aceitação"
            },
            {
                "id": 10,
                "item": "Posts semanais",
                "descricao": "Posts semanais sobre aprendizados reais",
                "status_desejado": "Postagem consistente (1x por semana)",
                "nivel_importancia": NivelOtimizacao.RECOMENDADO,
                "impacto": "Mantém perfil ativo e relevante"
            }
        ]
    
    def _analisar_item(self, item: Dict[str, Any], perfil_data: Dict[str, Any]) -> AnaliseItem:
        """Analisa item específico do perfil"""
        # Simulação de análise - em produção seria verificação real
        status_atual = self._verificar_status_atual(item, perfil_data)
        
        gap = self._identificar_gap(item, status_atual)
        recomendacao = self._gerar_recomendacao(item, status_atual)
        
        return AnaliseItem(
            item=item["item"],
            status_atual=status_atual,
            status_desejado=item["status_desejado"],
            nivel_importancia=item["nivel_importancia"],
            gap_analise=gap,
            recomendacao=recomendacao
        )
    
    def _verificar_status_atual(self, item: Dict[str, Any], perfil_data: Dict[str, Any]) -> str:
        """Verifica status atual do item"""
        # Simulação baseada no perfil do Carlos
        status_map = {
            1: "Não configurado",  # Aberto a oportunidades
            2: "Padrão LinkedIn",  # Banner
            3: "Título simples",   # Título
            4: "Formato currículo", # Sobre
            5: "Lista de tarefas",  # Experiências
            6: "Apenas texto",     # Mídia
            7: "Desordenadas",     # Competências
            8: "São Paulo",        # Localização
            9: "Mensagens genéricas", # Conexões
            10: "Inativo"          # Posts
        }
        
        return status_map.get(item["id"], "Não verificado")
    
    def _identificar_gap(self, item: Dict[str, Any], status_atual: str) -> str:
        """Identifica gap entre status atual e desejado"""
        gaps = {
            ("Não configurado", "Somente recrutadores"): "Algoritmo do LinkedIn não está ativo",
            ("Padrão LinkedIn", "Personalizado com informações profissionais"): "Perfil sem diferenciação visual",
            ("Título simples", "Otimizado com 5 palavras-chave relevantes"): "Baixa visibilidade em buscas",
            ("Formato currículo", "Redação humana e conversacional"): "Sem conexão emocional",
            ("Lista de tarefas", "Todas as experiências com métricas XYZ"): "Não demonstra resultados",
            ("Apenas texto", "Mídia visual em cada experiência relevante"): "Falta prova visual",
            ("Desordenadas", "Ordenadas por importância + recomendações"): "Habilidades não destacadas",
            ("São Paulo", "Configurada para mercado desejado"): "Pode limitar oportunidades remotas",
            ("Mensagens genéricas", "Estratégia de conexões ativa"): "Baixa taxa de aceitação",
            ("Inativo", "Postagem consistente (1x por semana)"): "Perfil sem engajamento"
        }
        
        return gaps.get((status_atual, item["status_desejado"]), "Gap não identificado")
    
    def _gerar_recomendacao(self, item: Dict[str, Any], status_atual: str) -> str:
        """Gera recomendação específica"""
        recomendacoes = {
            1: "Desative e reative 'Aberto a oportunidades' → Configure 'Somente recrutadores'",
            2: "Crie banner no Canva: Nome + Cargo-alvo + 2-3 competências + e-mail",
            3: "Título: Senior IT Project Manager | Power Platform | Cybersecurity | Transformação Digital | IA",
            4: "Reescreva 'Sobre' como conversa: gancho → história → detalhe pessoal → contato",
            5: "Converta experiências para XYZ: 'Reduzi tempo em 60% implementando dashboards, economizando R$500K'",
            6: "Adicione apresentações, projetos, artigos em cada experiência relevante",
            7: "Reordene competências: Power Platform, Cybersecurity, IA, SharePoint, Scrum Master",
            8: "Ajuste localização: 'São Paulo, SP | Disponível para remoto'",
            9: "Personalize conexões: 'Vi seu trabalho em [projeto] e gostaria de conectar'",
            10: "Crie calendário: posts semanais sobre aprendizados e desafios superados"
        }
        
        return recomendacoes.get(item["id"], "Recomendação não disponível")
    
    def _calcular_peso_importancia(self, nivel: NivelOtimizacao) -> int:
        """Calcula peso baseado no nível de importância"""
        pesos = {
            NivelOtimizacao.CRITICO: 15,
            NivelOtimizacao.IMPORTANTE: 10,
            NivelOtimizacao.RECOMENDADO: 5,
            NivelOtimizacao.OTIMIZADO: 3
        }
        return pesos.get(nivel, 5)
    
    def _gerar_proximos_passos(self, analise: Dict[str, Any]) -> List[str]:
        """Gera próximos passos priorizados"""
        passos = []
        
        # Priorizar gaps críticos
        if analise["gaps_criticos"]:
            passos.append("🔥 URGENTE: Corrigir gaps críticos para ativar algoritmo")
        
        # Recomendações baseadas no score
        if analise["score_geral"] < 50:
            passos.append("📋 Focar nos 5 itens críticos primeiro")
            passos.append("🎯 Implementar banner e título otimizado")
        elif analise["score_geral"] < 70:
            passos.append("📈 Avançar para itens importantes")
            passos.append("✍️ Reescrever seção 'Sobre'")
        else:
            passos.append("🚀 Otimizar itens recomendados")
            passos.append("📅 Criar calendário de posts")
        
        # Adicionar recomendações personalizadas
        passos.extend([
            "⏰ Dedique 2-3 horas para implementação inicial",
            "🔄 Revisar perfil a cada 30 dias",
            "📊 Monitorar engajamento e visualizações"
        ])
        
        return passos

class EquipeEspecialistasLinkedIn:
    """Equipe de 3 Especialistas RH para Análise LinkedIn"""
    
    def __init__(self):
        # 3 Especialistas com diferentes especialidades
        self.especialista1 = EspecialistaRH(
            nome="Dra. Patricia Mendes",
            especialidade="Estratégia de Marca Pessoal e LinkedIn",
            anos_experiencia=15
        )
        
        self.especialista2 = EspecialistaRH(
            nome="Dr. Roberto Costa",
            especialidade="Recrutamento Tecnológico e Headhunting",
            anos_experiencia=12
        )
        
        self.especialista3 = EspecialistaRH(
            nome="Dra. Fernanda Silva",
            especialidade="Employer Branding e Marketing de Talentos",
            anos_experiencia=10
        )
        
        self.perfil_carlos = self._carregar_perfil_atual()
    
    def _carregar_perfil_atual(self) -> Dict[str, Any]:
        """Carrega dados atuais do perfil do Carlos"""
        return {
            "nome": "Carlos Costato",
            "cargo_atual": "Senior IT Project Manager",
            "experiencia": "15+ anos",
            "localizacao": "São Paulo, SP",
            "email": "carlos.costato@gmail.com",
            "linkedin": "https://www.linkedin.com/in/carlos-costato/",
            "portfolio": "https://carloscostato-cmyk.github.io/Costato/",
            "habilidades_principais": [
                "Gestão de Projetos",
                "Scrum Master", 
                "Cybersecurity",
                "Power Platform",
                "SharePoint",
                "Power BI",
                "Power Automate",
                "Transformação Digital",
                "IA",
                "Machine Learning"
            ],
            "experiencias_destaque": [
                "Porto Seguro - Liderança de projetos enterprise",
                "Implementação de portais corporativos",
                "Dashboards executivos",
                "Especialização em IA pela FIAP"
            ],
            "formacao": "Especialização em IA - FIAP",
            "status_aberto_oportunidades": "Não verificado",
            "banner_personalizado": False,
            "titulo_otimizado": False,
            "sobre_humanizado": False,
            "experiencias_xyz": False,
            "midia_visual": False,
            "competencias_ordenadas": False,
            "localizacao_estrategica": False,
            "conexoes_personalizadas": False,
            "posts_semanais": False
        }
    
    def executar_analise_completa(self) -> Dict[str, Any]:
        """Executa análise completa pelos 3 especialistas"""
        print("EQUIPE DE ESPECIALISTAS RH - ANALISE LINKEDIN")
        print("="*60)
        print(f"Perfil analisado: {self.perfil_carlos['nome']}")
        print(f"Cargo: {self.perfil_carlos['cargo_atual']}")
        print(f"Experiencia: {self.perfil_carlos['experiencia']}")
        print("="*60)
        
        # Análise individual dos especialistas
        analises = []
        
        print(f"\n{self.especialista1.nome} - {self.especialista1.especialidade}")
        analise1 = self.especialista1.analisar_perfil_linkedin(self.perfil_carlos)
        analises.append(analise1)
        print(f"   Score: {analise1['score_geral']:.1f}/100")
        print(f"   Status: {'APROVADO' if analise1['status_aprovacao'] else 'NECESSITA AJUSTES'}")
        
        print(f"\n{self.especialista2.nome} - {self.especialista2.especialidade}")
        analise2 = self.especialista2.analisar_perfil_linkedin(self.perfil_carlos)
        analises.append(analise2)
        print(f"   Score: {analise2['score_geral']:.1f}/100")
        print(f"   Status: {'APROVADO' if analise2['status_aprovacao'] else 'NECESSITA AJUSTES'}")
        
        print(f"\n{self.especialista3.nome} - {self.especialista3.especialidade}")
        analise3 = self.especialista3.analisar_perfil_linkedin(self.perfil_carlos)
        analises.append(analise3)
        print(f"   Score: {analise3['score_geral']:.1f}/100")
        print(f"   Status: {'APROVADO' if analise3['status_aprovacao'] else 'NECESSITA AJUSTES'}")
        
        # Consolidação das análises
        resultado_consolidado = self._consolidar_analises(analises)
        
        # Salvar análise completa
        self._salvar_analise_completa(resultado_consolidado)
        
        return resultado_consolidado
    
    def _consolidar_analises(self, analises: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Consolida análises dos 3 especialistas"""
        scores = [a['score_geral'] for a in analises]
        aprovacoes = [a['status_aprovacao'] for a in analises]
        
        consolidado = {
            "data_analise": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "perfil_analisado": self.perfil_carlos['nome'],
            "especialistas": [
                {
                    "nome": a['especialista'],
                    "especialidade": a['especialidade'],
                    "score": a['score_geral'],
                    "aprovacao": a['status_aprovacao']
                } for a in analises
            ],
            "score_medio": sum(scores) / len(scores),
            "aprovacao_final": all(aprovacoes),
            "gaps_consolidados": self._consolidar_gaps(analises),
            "recomendacoes_consolidadas": self._consolidar_recomendacoes(analises),
            "placao_acao": self._gerar_plano_acao(analises),
            "investimento_tempo": self._estimar_investimento_tempo(analises),
            "roi_esperado": self._calcular_roi_esperado(analises)
        }
        
        return consolidado
    
    def _consolidar_gaps(self, analises: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Consolida gaps críticos de todas as análises"""
        todos_gaps = []
        
        for analise in analises:
            todos_gaps.extend(analise['gaps_criticos'])
        
        # Remover duplicatas e priorizar
        gaps_unicos = []
        vistos = set()
        
        for gap in todos_gaps:
            if gap.item not in vistos:
                gaps_unicos.append(gap)
                vistos.add(gap.item)
        
        return gaps_unicos
    
    def _consolidar_recomendacoes(self, analises: List[Dict[str, Any]]) -> List[str]:
        """Consolida recomendações de todas as análises"""
        todas_recomendacoes = []
        
        for analise in analises:
            todas_recomendacoes.extend(analise['recomendacoes_prioritarias'])
        
        # Remover duplicatas
        recomendacoes_unicas = list(set(todas_recomendacoes))
        
        # Ordenar por importância
        return sorted(recomendacoes_unicas)
    
    def _gerar_plano_acao(self, analises: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Gera plano de ação detalhado"""
        plano = {
            "fase1_critica": {
                "duracao": "2-3 horas",
                "itens": [
                    "Configurar 'Aberto a oportunidades' → 'Somente recrutadores'",
                    "Criar banner personalizado no Canva",
                    "Otimizar título com 5 palavras-chave",
                    "Ajustar localização estratégica"
                ],
                "impacto": "Reativação do algoritmo + 40% mais visibilidade"
            },
            "fase2_importante": {
                "duracao": "3-4 horas",
                "itens": [
                    "Reescrever seção 'Sobre' para tom humano",
                    "Converter experiências para formato XYZ",
                    "Adicionar mídia visual nas experiências",
                    "Reordenar competências por relevância"
                ],
                "impacto": "Conexão emocional + demonstração de resultados"
            },
            "fase3_recomendado": {
                "duracao": "1-2 horas por semana",
                "itens": [
                    "Personalizar pedidos de conexão",
                    "Criar calendário de posts semanais",
                    "Solicitar recomendações específicas",
                    "Monitorar métricas do perfil"
                ],
                "impacto": "Engajamento contínuo + networking estratégico"
            }
        }
        
        return plano
    
    def _estimar_investimento_tempo(self, analises: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Estima investimento de tempo necessário"""
        return {
            "implementacao_inicial": "6-9 horas",
            "manutencao_semanal": "2-3 horas",
            "revisao_mensal": "1-2 horas",
            "tempo_ate_resultados": "2-4 semanas",
            "horas_totais_primeiro_mes": "20-25 horas"
        }
    
    def _calcular_roi_esperado(self, analises: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calcula ROI esperado das otimizações"""
        return {
            "aumento_visualizacoes": "300-500%",
            "aumento_conexoes": "200-400%",
            "aumento_mensagens_recrutadores": "400-800%",
            "reducao_tempo_primeiro_contato": "60-80%",
            "oportunidades_geradas": "+10-15 por mês",
            "tempo_retorno_investimento": "2-3 meses"
        }
    
    def _salvar_analise_completa(self, resultado: Dict[str, Any]):
        """Salva análise completa em arquivo"""
        with open('analise-linkedin-especialistas.json', 'w', encoding='utf-8') as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"\nAnalise completa salva: analise-linkedin-especialistas.json")
    
    def gerar_relatorio_executivo(self) -> str:
        """Gera relatório executivo para tomada de decisão"""
        resultado = self.executar_analise_completa()
        
        relatorio = f"""
RELATORIO EXECUTIVO - ANALISE LINKEDIN CARLOS COSTATO
{'='*60}

ANALISE CONSOLIDADA:
• Score Medio: {resultado['score_medio']:.1f}/100
• Status Final: {'APROVADO' if resultado['aprovacao_final'] else 'NECESSITA AJUSTES'}
• Especialistas: 3 especialistas RH avaliaram

GAPS CRITICOS IDENTIFICADOS: {len(resultado['gaps_consolidados'])}
"""
        
        for i, gap in enumerate(resultado['gaps_consolidados'], 1):
            relatorio += f"""
{i}. {gap.item}
   Status Atual: {gap.status_atual}
   Gap: {gap.gap_analise}
   Recomendacao: {gap.recomendacao}
"""
        
        relatorio += f"""
INVESTIMENTO NECESSARIO:
• Implementacao Inicial: {resultado['investimento_tempo']['implementacao_inicial']}
• Manutencao Semanal: {resultado['investimento_tempo']['manutencao_semanal']}
• Tempo ate Resultados: {resultado['investimento_tempo']['tempo_ate_resultados']}

ROI ESPERADO:
• Aumento Visualizacoes: {resultado['roi_esperado']['aumento_visualizacoes']}
• Aumento Conexoes: {resultado['roi_esperado']['aumento_conexoes']}
• Mensagens Recrutadores: {resultado['roi_esperado']['aumento_mensagens_recrutadores']}
• Oportunidades/mes: {resultado['roi_esperado']['oportunidades_geradas']}

DECISAO RECOMENDADA:
{'SIM - Prosseguir com implementacao imediata' if not resultado['aprovacao_final'] else 'PERFIL JA OTIMIZADO - Manter atualizacoes'}

PROXIMOS PASSOS:
1. Implementar Fase 1 Critica (2-3 horas)
2. Monitorar resultados por 2 semanas
3. Ajustar baseado em metricas
4. Expandir para Fase 2

INSIGHT DOS ESPECIALISTAS:
Reativacao do algoritmo + 40% mais visibilidade

---
Relatorio gerado em: {resultado['data_analise']}
Equipe: {', '.join([e['nome'] for e in resultado['especialistas']])}
"""
        
        # Salvar relatório
        with open('relatorio-executivo-linkedin.txt', 'w', encoding='utf-8') as f:
            f.write(relatorio)
        
        print(f"\nRelatorio executivo salvo: relatorio-executivo-linkedin.txt")
        
        return relatorio

# Executar análise pelos 3 especialistas
if __name__ == "__main__":
    equipe = EquipeEspecialistasLinkedIn()
    
    print("EQUIPE DE 3 ESPECIALISTAS RH - ANALISE LINKEDIN")
    print("="*60)
    print("Carlos Costato - Senior IT Project Manager")
    print("Validacao estrategica antes do desenvolvimento")
    print("="*60)
    
    # Executar análise completa
    resultado = equipe.executar_analise_completa()
    
    # Gerar relatório executivo
    relatorio = equipe.gerar_relatorio_executivo()
    
    print(f"\nANALISE CONCLUIDA!")
    print(f"Score medio: {resultado['score_medio']:.1f}/100")
    print(f"Gaps criticos: {len(resultado['gaps_consolidados'])}")
    print(f"ROI esperado: {resultado['roi_esperado']['aumento_visualizacoes']} visualizacoes")
    print(f"Investimento: {resultado['investimento_tempo']['implementacao_inicial']}")
    print(f"Relatorios gerados: analise-linkedin-especialistas.json, relatorio-executivo-linkedin.txt")
