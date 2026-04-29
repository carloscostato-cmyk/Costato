#!/usr/bin/env python3
"""
🔍 3 ESPECIALISTAS EM DIAGNÓSTICO - BOTÃO DOWNLOAD CV
Carlos Costato - Sistema de Diagnóstico Real de Erros
"""

import subprocess
import json
import time
import os
from datetime import datetime
from typing import Dict, List, Any
import webbrowser
import requests
from urllib.parse import quote

class EspecialistaDiagnosticoDownload:
    """Especialista em diagnosticar problemas reais do download"""
    
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        diagnosticos_realizados = 0
        problemas_encontrados = []
        solucoes_propostas = []
    
    def verificar_arquivo_fisico(self) -> Dict[str, Any]:
        """Verificação física do arquivo PDF"""
        try:
            caminho_completo = r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato\curriculo de carlos costato.pdf"
            
            resultado = {
                "teste": "Verificação Física do Arquivo",
                "caminho_testado": caminho_completo,
                "status": "ERRO",
                "detalhes": {}
            }
            
            # Verificar se arquivo existe
            if os.path.exists(caminho_completo):
                resultado["status"] = "SUCESSO"
                resultado["detalhes"]["existe"] = True
                resultado["detalhes"]["tamanho_bytes"] = os.path.getsize(caminho_completo)
                resultado["detalhes"]["tamanho_mb"] = round(os.path.getsize(caminho_completo) / (1024 * 1024), 2)
                resultado["detalhes"]["data_modificacao"] = datetime.fromtimestamp(os.path.getmtime(caminho_completo)).strftime('%Y-%m-%d %H:%M:%S')
                resultado["mensagem"] = f"Arquivo encontrado ({resultado['detalhes']['tamanho_mb']} MB)"
            else:
                resultado["detalhes"]["existe"] = False
                resultado["mensagem"] = "Arquivo NÃO encontrado no caminho especificado"
                
                # Tentar encontrar arquivos PDF similares
                diretorio = os.path.dirname(caminho_completo)
                arquivos_pdf = []
                try:
                    for arquivo in os.listdir(diretorio):
                        if arquivo.lower().endswith('.pdf'):
                            arquivos_pdf.append(arquivo)
                    resultado["detalhes"]["arquivos_pdf_encontrados"] = arquivos_pdf
                except Exception as e:
                    resultado["detalhes"]["erro_lista"] = str(e)
            
            return resultado
            
        except Exception as e:
            return {
                "teste": "Verificação Física do Arquivo",
                "status": "ERRO",
                "mensagem": f"Erro na verificação: {str(e)}"
            }
    
    def testar_acesso_navegador(self) -> Dict[str, Any]:
        """Testa acesso via navegador simulando uso real"""
        try:
            resultado = {
                "teste": "Acesso via Navegador",
                "status": "ERRO",
                "detalhes": {}
            }
            
            # Testar diferentes URLs
            urls_testadas = [
                "curriculo de carlos costato.pdf",
                "curriculo%20de%20carlos%20costato.pdf",
                quote("curriculo de carlos costato.pdf"),
                "./curriculo de carlos costato.pdf",
                "./curriculo%20de%20carlos%20costato.pdf"
            ]
            
            resultados_urls = []
            
            for url in urls_testadas:
                try:
                    # Tentar abrir arquivo local
                    caminho_completo = os.path.join(
                        r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato",
                        url.replace('%20', ' ').replace('./', '')
                    )
                    
                    if os.path.exists(caminho_completo):
                        resultados_urls.append({
                            "url": url,
                            "status": "SUCESSO",
                            "caminho_resolvido": caminho_completo,
                            "mensagem": "Acesso bem-sucedido"
                        })
                    else:
                        resultados_urls.append({
                            "url": url,
                            "status": "FALHA",
                            "mensagem": "Arquivo não encontrado"
                        })
                        
                except Exception as e:
                    resultados_urls.append({
                        "url": url,
                        "status": "ERRO",
                        "mensagem": str(e)
                    })
            
            resultado["detalhes"]["urls_testadas"] = resultados_urls
            
            # Verificar se alguma URL funcionou
            sucessos = [r for r in resultados_urls if r["status"] == "SUCESSO"]
            if sucessos:
                resultado["status"] = "PARCIAL"
                resultado["mensagem"] = f"{len(sucessos)} de {len(urls_testadas)} URLs funcionam"
                resultado["detalhes"]["urls_funcionando"] = [s["url"] for s in sucessos]
            else:
                resultado["status"] = "ERRO"
                resultado["mensagem"] = "Nenhuma URL funciona para acesso ao arquivo"
            
            return resultado
            
        except Exception as e:
            return {
                "teste": "Acesso via Navegador",
                "status": "ERRO",
                "mensagem": f"Erro no teste: {str(e)}"
            }
    
    def analisar_codigo_javascript(self) -> Dict[str, Any]:
        """Analisa o código JavaScript em busca de problemas"""
        try:
            resultado = {
                "teste": "Análise de Código JavaScript",
                "status": "ERRO",
                "detalhes": {}
            }
            
            # Ler o arquivo HTML
            caminho_html = r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato\teste_voz.html"
            
            if not os.path.exists(caminho_html):
                resultado["mensagem"] = "Arquivo HTML não encontrado"
                return resultado
            
            with open(caminho_html, 'r', encoding='utf-8') as f:
                conteudo_html = f.read()
            
            # Analisar a função downloadCV
            problemas_encontrados = []
            
            # Verificar se a função existe
            if "function downloadCV()" not in conteudo_html:
                problemas_encontrados.append("Função downloadCV() não encontrada")
            else:
                # Extrair a função
                inicio_func = conteudo_html.find("function downloadCV()")
                if inicio_func != -1:
                    # Encontrar o fim da função
                    fim_func = conteudo_html.find("}", inicio_func + 100)
                    if fim_func != -1:
                        funcao_completa = conteudo_html[inicio_func:fim_func+1]
                        
                        # Analisar problemas comuns
                        if "const cvPath" in funcao_completa:
                            # Extrair o caminho
                            inicio_path = funcao_completa.find("const cvPath = '") + len("const cvPath = '")
                            fim_path = funcao_completa.find("'", inicio_path)
                            if fim_path != -1:
                                caminho_usado = funcao_completa[inicio_path:fim_path]
                                resultado["detalhes"]["caminho_usado_no_codigo"] = caminho_usado
                                
                                # Verificar se o caminho corresponde ao arquivo real
                                caminho_completo_teste = os.path.join(
                                    r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato",
                                    caminho_usado.replace('%20', ' ')
                                )
                                
                                if not os.path.exists(caminho_completo_teste):
                                    problemas_encontrados.append(f"Caminho no código '{caminho_usado}' não corresponde a arquivo existente")
                        
                        # Verificar tratamento de erros
                        if "try {" not in funcao_completa:
                            problemas_encontrados.append("Função não tem tratamento de erros")
                        
                        # Verificar feedback visual
                        if "downloadBtn.innerHTML" not in funcao_completa:
                            problemas_encontrados.append("Função não fornece feedback visual")
            
            if problemas_encontrados:
                resultado["status"] = "ERRO"
                resultado["mensagem"] = f"{len(problemas_encontrados)} problemas encontrados"
                resultado["detalhes"]["problemas"] = problemas_encontrados
            else:
                resultado["status"] = "SUCESSO"
                resultado["mensagem"] = "Código JavaScript parece correto"
            
            return resultado
            
        except Exception as e:
            return {
                "teste": "Análise de Código JavaScript",
                "status": "ERRO",
                "mensagem": f"Erro na análise: {str(e)}"
            }
    
    def simular_download_real(self) -> Dict[str, Any]:
        """Simula o processo real de download"""
        try:
            resultado = {
                "teste": "Simulação de Download Real",
                "status": "ERRO",
                "detalhes": {}
            }
            
            # Criar script de teste HTML
            script_teste = """
<!DOCTYPE html>
<html>
<head>
    <title>Teste Download CV</title>
</head>
<body>
    <h1>Teste de Download CV</h1>
    <button onclick="testarDownload()">Testar Download</button>
    <div id="resultado"></div>
    
    <script>
        function testarDownload() {
            const resultado = document.getElementById('resultado');
            resultado.innerHTML = 'Iniciando teste...';
            
            try {
                // Simular exatamente o código do site
                const cvPath = 'curriculo%20de%20carlos%20costato.pdf';
                const link = document.createElement('a');
                link.href = cvPath;
                link.download = 'Carlos_Costato_CV.pdf';
                link.style.display = 'none';
                
                document.body.appendChild(link);
                
                // Verificar se o link foi criado corretamente
                resultado.innerHTML += '<br>Link criado: ' + link.href;
                resultado.innerHTML += '<br>Download attribute: ' + link.download;
                
                // Tentar verificar se o arquivo existe
                fetch(cvPath, {method: 'HEAD'})
                    .then(response => {
                        resultado.innerHTML += '<br>Status HTTP: ' + response.status;
                        if (response.ok) {
                            resultado.innerHTML += '<br><strong>SUCESSO: Arquivo encontrado!</strong>';
                        } else {
                            resultado.innerHTML += '<br><strong>ERRO: Arquivo não encontrado!</strong>';
                        }
                    })
                    .catch(error => {
                        resultado.innerHTML += '<br><strong>ERRO: ' + error.message + '</strong>';
                    });
                
                // Limpar
                setTimeout(() => {
                    document.body.removeChild(link);
                }, 1000);
                
            } catch (error) {
                resultado.innerHTML += '<br><strong>ERRO: ' + error.message + '</strong>';
            }
        }
    </script>
</body>
</html>
            """
            
            # Salvar script de teste
            caminho_teste = r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato\teste_download_cv.html"
            with open(caminho_teste, 'w', encoding='utf-8') as f:
                f.write(script_teste)
            
            resultado["detalhes"]["script_gerado"] = caminho_teste
            resultado["detalhes"]["instrucoes"] = "Abra o arquivo teste_download_cv.html no navegador para testar"
            
            # Tentar verificar via HTTP request
            try:
                import http.server
                import socketserver
                import threading
                
                PORT = 8001
                
                def iniciar_servidor():
                    os.chdir(r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato")
                    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
                        httpd.serve_forever()
                
                servidor_thread = threading.Thread(target=iniciar_servidor, daemon=True)
                servidor_thread.start()
                time.sleep(1)
                
                # Testar requisição
                url_teste = f"http://localhost:{PORT}/curriculo%20de%20carlos%20costato.pdf"
                response = requests.get(url_teste, timeout=3)
                
                resultado["detalhes"]["teste_http"] = {
                    "url": url_teste,
                    "status_code": response.status_code,
                    "content_length": len(response.content),
                    "sucesso": response.status_code == 200
                }
                
                if response.status_code == 200:
                    resultado["status"] = "SUCESSO"
                    resultado["mensagem"] = "Download simulado funcionou via HTTP"
                else:
                    resultado["status"] = "ERRO"
                    resultado["mensagem"] = f"Erro HTTP: {response.status_code}"
                    
            except Exception as e:
                resultado["detalhes"]["erro_http"] = str(e)
                resultado["mensagem"] = f"Não foi possível testar via HTTP: {str(e)}"
            
            return resultado
            
        except Exception as e:
            return {
                "teste": "Simulação de Download Real",
                "status": "ERRO",
                "mensagem": f"Erro na simulação: {str(e)}"
            }
    
    def executar_diagnostico_completo(self) -> Dict[str, Any]:
        """Executa diagnóstico completo com todos os testes"""
        print(f"\n🔍 {self.nome} - Iniciando diagnóstico completo...")
        
        resultado_agente = {
            "agente": self.nome,
            "especialidade": self.especialidade,
            "data_diagnostico": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "testes": []
        }
        
        # Executar todos os testes
        testes = [
            self.verificar_arquivo_fisico,
            self.testar_acesso_navegador,
            self.analisar_codigo_javascript,
            self.simular_download_real
        ]
        
        for teste in testes:
            print(f"   🧪 Executando {teste.__name__}...")
            resultado_teste = teste()
            resultado_agente["testes"].append(resultado_teste)
            
            if resultado_teste["status"] == "SUCESSO":
                print(f"      ✅ {resultado_teste['mensagem']}")
            else:
                print(f"      ❌ {resultado_teste['mensagem']}")
        
        # Calcular estatísticas
        total_testes = len(resultado_agente["testes"])
        testes_sucesso = sum(1 for t in resultado_agente["testes"] if t["status"] == "SUCESSO")
        testes_erro = sum(1 for t in resultado_agente["testes"] if t["status"] == "ERRO")
        testes_parcial = sum(1 for t in resultado_agente["testes"] if t["status"] == "PARCIAL")
        
        resultado_agente["estatisticas"] = {
            "total_testes": total_testes,
            "testes_sucesso": testes_sucesso,
            "testes_erro": testes_erro,
            "testes_parcial": testes_parcial,
            "taxa_sucesso": round((testes_sucesso / total_testes) * 100, 1) if total_testes > 0 else 0
        }
        
        # Determinar status geral
        if testes_erro > 0:
            resultado_agente["status_geral"] = "PROBLEMAS_ENCONTRADOS"
        elif testes_parcial > 0:
            resultado_agente["status_geral"] = "FUNCIONA_PARCIALMENTE"
        else:
            resultado_agente["status_geral"] = "FUNCIONANDO_BEM"
        
        return resultado_agente

class EquipeEspecialistasDiagnostico:
    """Equipe de 3 Especialistas em Diagnóstico de Download"""
    
    def __init__(self):
        # 3 Especialistas em Diagnóstico
        self.especialista1 = EspecialistaDiagnosticoDownload(
            nome="Rafael Sistemas",
            especialidade="Especialista em Análise de Sistemas e Arquivos"
        )
        
        self.especialista2 = EspecialistaDiagnosticoDownload(
            nome="Camila Frontend",
            especialidade="Especialista em Frontend e Experiência do Usuário"
        )
        
        self.especialista3 = EspecialistaDiagnosticoDownload(
            nome="Bruno Infra",
            especialidade="Especialista em Infraestrutura e Deploy"
        )
        
        self.resultados_equipe = []
    
    def executar_diagnostico_completo(self) -> Dict[str, Any]:
        """Executa diagnóstico completo com todos os especialistas"""
        print("🔍 EQUIPE DE 3 ESPECIALISTAS - DIAGNÓSTICO DOWNLOAD CV")
        print("="*60)
        print(f"👥 Especialista 1: {self.especialista1.nome}")
        print(f"👥 Especialista 2: {self.especialista2.nome}")
        print(f"👥 Especialista 3: {self.especialista3.nome}")
        print("="*60)
        
        resultado_final = {
            "data_execucao": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "especialistas": [
                self.especialista1.nome,
                self.especialista2.nome,
                self.especialista3.nome
            ],
            "resultados": [],
            "problemas_comuns": [],
            "solucoes_recomendadas": [],
            "status_final": "PENDENTE"
        }
        
        # Executar diagnóstico com cada especialista
        especialistas = [self.especialista1, self.especialista2, self.especialista3]
        
        for especialista in especialistas:
            resultado_agente = especialista.executar_diagnostico_completo()
            resultado_final["resultados"].append(resultado_agente)
        
        # Analisar problemas comuns
        problemas_comuns = self._identificar_problemas_comuns(resultado_final)
        resultado_final["problemas_comuns"] = problemas_comuns
        
        # Gerar soluções recomendadas
        solucoes = self._gerar_solucoes_recomendadas(problemas_comuns)
        resultado_final["solucoes_recomendadas"] = solucoes
        
        # Determinar status final
        status_agente1 = resultado_final["resultados"][0]["status_geral"]
        status_agente2 = resultado_final["resultados"][1]["status_geral"]
        status_agente3 = resultado_final["resultados"][2]["status_geral"]
        
        if "PROBLEMAS_ENCONTRADOS" in [status_agente1, status_agente2, status_agente3]:
            resultado_final["status_final"] = "PROBLEMAS_CRITICOS"
        elif "FUNCIONA_PARCIALMENTE" in [status_agente1, status_agente2, status_agente3]:
            resultado_final["status_final"] = "NECESSITA_CORRECOES"
        else:
            resultado_final["status_final"] = "FUNCIONANDO"
        
        # Salvar resultados
        self.resultados_equipe.append(resultado_final)
        self._salvar_resultados()
        
        return resultado_final
    
    def _identificar_problemas_comuns(self, resultado: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifica problemas comuns entre os especialistas"""
        problemas = []
        
        # Coletar todos os problemas
        todos_problemas = []
        for resultado_agente in resultado["resultados"]:
            for teste in resultado_agente["testes"]:
                if teste["status"] in ["ERRO", "FALHA"]:
                    todos_problemas.append({
                        "teste": teste["teste"],
                        "mensagem": teste["mensagem"],
                        "agente": resultado_agente["agente"]
                    })
        
        # Agrupar problemas por tipo
        problemas_por_teste = {}
        for problema in todos_problemas:
            nome_teste = problema["teste"]
            if nome_teste not in problemas_por_teste:
                problemas_por_teste[nome_teste] = []
            problemas_por_teste[nome_teste].append(problema)
        
        # Identificar problemas comuns (mencionados por múltiplos especialistas)
        for nome_teste, lista_problemas in problemas_por_teste.items():
            if len(lista_problemas) >= 2:  # Problema mencionado por 2+ especialistas
                problemas.append({
                    "tipo": nome_teste,
                    "frequencia": len(lista_problemas),
                    "descricao": lista_problemas[0]["mensagem"],
                    "agentes": [p["agente"] for p in lista_problemas]
                })
        
        return problemas
    
    def _gerar_solucoes_recomendadas(self, problemas: List[Dict[str, Any]]) -> List[str]:
        """Gera soluções baseadas nos problemas encontrados"""
        solucoes = []
        
        for problema in problemas:
            if "Arquivo não encontrado" in problema["descricao"]:
                solucoes.append("Verificar se o arquivo PDF existe no diretório correto")
                solucoes.append("Confirmar o nome exato do arquivo (case sensitive)")
            elif "caminho" in problema["descricao"].lower():
                solucoes.append("Corrigir o caminho do arquivo no código JavaScript")
                solucoes.append("Usar URL encoding para espaços e caracteres especiais")
            elif "HTTP" in problema["descricao"]:
                solucoes.append("Configurar servidor para servir arquivos estáticos")
                solucoes.append("Verificar permissões de acesso aos arquivos")
            elif "JavaScript" in problema["descricao"]:
                solucoes.append("Revisar implementação da função downloadCV()")
                solucoes.append("Adicionar tratamento de erros robusto")
        
        if not solucoes:
            solucoes.append("Sistema parece funcionar corretamente")
        
        return solucoes
    
    def _salvar_resultados(self):
        """Salva resultados do diagnóstico"""
        try:
            with open('diagnostico-download-cv.json', 'w', encoding='utf-8') as f:
                json.dump(self.resultados_equipe, f, ensure_ascii=False, indent=2, default=str)
            print(f"\n💾 Diagnóstico salvo: diagnostico-download-cv.json")
        except Exception as e:
            print(f"\n❌ Erro ao salvar diagnóstico: {e}")
    
    def gerar_relatorio_diagnostico(self) -> str:
        """Gera relatório completo do diagnóstico"""
        resultado = self.executar_diagnostico_completo()
        
        relatorio = f"""
🔍 RELATORIO DE DIAGNOSTICO - BOTAO DOWNLOAD CV
{'='*60}

Data: {resultado['data_execucao']}
Especialistas: {', '.join(resultado['especialistas'])}
Status Final: {resultado['status_final']}

RESULTADOS POR ESPECIALISTA:
"""
        
        for i, resultado_agente in enumerate(resultado['resultados'], 1):
            relatorio += f"""
{i}. {resultado_agente['agente']} - {resultado_agente['especialidade']}
   Data: {resultado_agente['data_diagnostico']}
   Status Geral: {resultado_agente['status_geral']}
   Taxa de Sucesso: {resultado_agente['estatisticas']['taxa_sucesso']}%
   
   Testes Realizados:
"""
            for teste in resultado_agente['testes']:
                status_icon = "✅" if teste['status'] == 'SUCESSO' else "❌" if teste['status'] == 'ERRO' else "⚠️"
                relatorio += f"   {status_icon} {teste['teste']}: {teste['mensagem']}\n"
        
        relatorio += f"""
PROBLEMAS COMUNS IDENTIFICADOS:
"""
        if resultado['problemas_comuns']:
            for problema in resultado['problemas_comuns']:
                relatorio += f"• {problema['tipo']}: {problema['descricao']} (mencionado por {problema['frequencia']} especialistas)\n"
        else:
            relatorio += "• Nenhum problema crítico identificado\n"
        
        relatorio += f"""
SOLUCOES RECOMENDADAS:
"""
        for solucao in resultado['solucoes_recomendadas']:
            relatorio += f"• {solucao}\n"
        
        relatorio += f"""
CONCLUSAO:
Diagnostico {'concluido com problemas criticos' if resultado['status_final'] == 'PROBLEMAS_CRITICOS' else 'concluido - necessita atencão' if resultado['status_final'] == 'NECESSITA_CORRECOES' else 'concluido - funcionando bem'}.

{'ACAO RECOMENDADA: Corrigir problemas identificados antes de prosseguir.' if resultado['status_final'] != 'FUNCIONANDO' else 'ACAO RECOMENDADA: Sistema pronto para uso.'}

---
Relatorio gerado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Sistema: Equipe de Especialistas em Diagnostico v1.0
"""
        
        # Salvar relatório
        with open('relatorio-diagnostico-download.txt', 'w', encoding='utf-8') as f:
            f.write(relatorio)
        
        print(f"\n📋 Relatório salvo: relatorio-diagnostico-download.txt")
        
        return relatorio

# Executar diagnóstico
if __name__ == "__main__":
    equipe = EquipeEspecialistasDiagnostico()
    
    print("🔍 EQUIPE DE 3 ESPECIALISTAS - DIAGNÓSTICO DOWNLOAD CV")
    print("="*60)
    print("Carlos Costato - Sistema de Diagnóstico Real de Erros")
    print("="*60)
    
    # Executar diagnóstico completo
    relatorio = equipe.gerar_relatorio_diagnostico()
    
    print(f"\n🎉 DIAGNÓSTICO CONCLUÍDO!")
    print(f"📋 Relatório completo: relatorio-diagnostico-download.txt")
    print(f"💾 Dados detalhados: diagnostico-download-cv.json")
    print(f"🔍 Verifique o relatório para identificar e corrigir os problemas")
