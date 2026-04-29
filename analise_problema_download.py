#!/usr/bin/env python3
"""
🔍 ANÁLISE DO PROBLEMA DE DOWNLOAD
Carlos Costato - Diagnóstico Real da Dificuldade
"""

import os
import subprocess
from datetime import datetime
from typing import Dict, List, Any

class AnalisadorProblemaDownload:
    """Analisador especializado em identificar a raiz do problema de download"""
    
    def __init__(self):
        self.diretorio_atual = r"c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Costato"
        self.arquivo_pdf = "curriculo de carlos costato.pdf"
        self.caminho_completo = os.path.join(self.diretorio_atual, self.arquivo_pdf)
    
    def analisar_situacao_atual(self) -> Dict[str, Any]:
        """Análise completa da situação atual"""
        print("🔍 ANÁLISE DO PROBLEMA DE DOWNLOAD")
        print("="*60)
        print("Carlos Costato - Diagnóstico Real da Dificuldade")
        print("="*60)
        
        analise = {
            "data_analise": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "problema_identificado": "",
            "causas_possiveis": [],
            "situacao_arquivo": {},
            "situacao_codigo": {},
            "recomendacao": ""
        }
        
        # 1. Verificar situação do arquivo
        print("\n📁 1. VERIFICAÇÃO DO ARQUIVO PDF")
        situacao_arquivo = self._verificar_situacao_arquivo()
        analise["situacao_arquivo"] = situacao_arquivo
        
        # 2. Verificar situação do código
        print("\n💻 2. VERIFICAÇÃO DO CÓDIGO")
        situacao_codigo = self._verificar_situacao_codigo()
        analise["situacao_codigo"] = situacao_codigo
        
        # 3. Identificar problema principal
        print("\n🎯 3. IDENTIFICAÇÃO DO PROBLEMA")
        problema = self._identificar_problema_principal(situacao_arquivo, situacao_codigo)
        analise["problema_identificado"] = problema
        
        # 4. Analisar causas possíveis
        print("\n🔍 4. ANÁLISE DAS CAUSAS")
        causas = self._analisar_causas_possiveis(situacao_arquivo, situacao_codigo)
        analise["causas_possiveis"] = causas
        
        # 5. Gerar recomendação
        print("\n💡 5. RECOMENDAÇÃO")
        recomendacao = self._gerar_recomendacao(problema, causas)
        analise["recomendacao"] = recomendacao
        
        return analise
    
    def _verificar_situacao_arquivo(self) -> Dict[str, Any]:
        """Verifica situação detalhada do arquivo PDF"""
        resultado = {
            "existe": False,
            "caminho_testado": self.caminho_completo,
            "tamanho_bytes": 0,
            "tamanho_mb": 0,
            "data_modificacao": "",
            "permissoes": "",
            "problemas": []
        }
        
        try:
            if os.path.exists(self.caminho_completo):
                resultado["existe"] = True
                resultado["tamanho_bytes"] = os.path.getsize(self.caminho_completo)
                resultado["tamanho_mb"] = round(resultado["tamanho_bytes"] / (1024 * 1024), 2)
                resultado["data_modificacao"] = datetime.fromtimestamp(os.path.getmtime(self.caminho_completo)).strftime('%Y-%m-%d %H:%M:%S')
                
                # Verificar permissões
                if os.access(self.caminho_completo, os.R_OK):
                    resultado["permissoes"] = "LEITURA OK"
                else:
                    resultado["permissoes"] = "SEM PERMISSÃO DE LEITURA"
                    resultado["problemas"].append("Arquivo não pode ser lido")
                
                print(f"   ✅ Arquivo encontrado: {resultado['tamanho_mb']} MB")
                print(f"   📅 Modificado: {resultado['data_modificacao']}")
                print(f"   🔐 Permissões: {resultado['permissoes']}")
                
            else:
                resultado["problemas"].append("Arquivo não encontrado no caminho especificado")
                print(f"   ❌ Arquivo NÃO encontrado")
                print(f"   📁 Caminho testado: {self.caminho_completo}")
                
                # Listar arquivos PDF no diretório
                try:
                    arquivos_pdf = []
                    for arquivo in os.listdir(self.diretorio_atual):
                        if arquivo.lower().endswith('.pdf'):
                            arquivos_pdf.append(arquivo)
                    
                    if arquivos_pdf:
                        print(f"   📄 PDFs encontrados: {len(arquivos_pdf)}")
                        for pdf in arquivos_pdf[:5]:  # Mostrar até 5
                            print(f"      - {pdf}")
                        if len(arquivos_pdf) > 5:
                            print(f"      ... e mais {len(arquivos_pdf) - 5}")
                    else:
                        print(f"   ❌ Nenhum arquivo PDF encontrado no diretório")
                        
                except Exception as e:
                    print(f"   ❌ Erro ao listar diretório: {e}")
                    resultado["problemas"].append(f"Erro ao acessar diretório: {e}")
                    
        except Exception as e:
            resultado["problemas"].append(f"Erro geral: {str(e)}")
            print(f"   ❌ Erro: {e}")
        
        return resultado
    
    def _verificar_situacao_codigo(self) -> Dict[str, Any]:
        """Verifica situação do código JavaScript"""
        resultado = {
            "funcao_existe": False,
            "caminho_usado": "",
            "tratamento_erros": False,
            "feedback_visual": False,
            "problemas": []
        }
        
        try:
            # Ler arquivo HTML
            caminho_html = os.path.join(self.diretorio_atual, "teste_voz.html")
            
            if not os.path.exists(caminho_html):
                resultado["problemas"].append("Arquivo teste_voz.html não encontrado")
                print(f"   ❌ Arquivo HTML não encontrado")
                return resultado
            
            with open(caminho_html, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Verificar se função existe
            if "function downloadCV()" in conteudo:
                resultado["funcao_existe"] = True
                print(f"   ✅ Função downloadCV() encontrada")
                
                # Extrair caminho usado
                inicio_path = conteudo.find("const cvPath = '") + len("const cvPath = '")
                if inicio_path > len("const cvPath = '"):
                    fim_path = conteudo.find("'", inicio_path)
                    if fim_path > inicio_path:
                        resultado["caminho_usado"] = conteudo[inicio_path:fim_path]
                        print(f"   📁 Caminho no código: '{resultado['caminho_usado']}'")
                
                # Verificar tratamento de erros
                if "try {" in conteudo and "catch" in conteudo:
                    resultado["tratamento_erros"] = True
                    print(f"   ✅ Tratamento de erros presente")
                else:
                    resultado["problemas"].append("Sem tratamento de erros")
                    print(f"   ⚠️ Sem tratamento de erros")
                
                # Verificar feedback visual
                if "downloadBtn.innerHTML" in conteudo:
                    resultado["feedback_visual"] = True
                    print(f"   ✅ Feedback visual presente")
                else:
                    resultado["problemas"].append("Sem feedback visual")
                    print(f"   ⚠️ Sem feedback visual")
                    
            else:
                resultado["problemas"].append("Função downloadCV() não encontrada")
                print(f"   ❌ Função downloadCV() NÃO encontrada")
                
        except Exception as e:
            resultado["problemas"].append(f"Erro ao analisar código: {str(e)}")
            print(f"   ❌ Erro: {e}")
        
        return resultado
    
    def _identificar_problema_principal(self, situacao_arquivo: Dict, situacao_codigo: Dict) -> str:
        """Identifica o problema principal"""
        problemas_arquivo = situacao_arquivo.get("problemas", [])
        problemas_codigo = situacao_codigo.get("problemas", [])
        
        if not situacao_arquivo.get("existe", False):
            return "ARQUIVO PDF NÃO ENCONTRADO"
        
        if "SEM PERMISSÃO DE LEITURA" in situacao_arquivo.get("permissoes", ""):
            return "ARQUIVO SEM PERMISSÃO DE ACESSO"
        
        if not situacao_codigo.get("funcao_existe", False):
            return "FUNÇÃO DOWNLOAD NÃO EXISTE"
        
        if situacao_codigo.get("caminho_usado", "") != situacao_arquivo.get("caminho_testado", ""):
            return "DESCOMPATIBILIDADE DE CAMINHO"
        
        if problemas_codigo:
            return "PROBLEMAS NO CÓDIGO JAVASCRIPT"
        
        return "PROBLEMA NÃO IDENTIFICADO"
    
    def _analisar_causas_possiveis(self, situacao_arquivo: Dict, situacao_codigo: Dict) -> List[str]:
        """Analisa causas possíveis do problema"""
        causas = []
        
        if not situacao_arquivo.get("existe", False):
            causas.append("Arquivo PDF não está no diretório correto")
            causas.append("Nome do arquivo pode estar diferente")
            causas.append("Arquivo pode ter sido movido ou excluído")
        
        if situacao_codigo.get("caminho_usado", ""):
            caminho_codigo = situacao_codigo["caminho_usado"]
            if "%20" in caminho_codigo:
                causas.append("URL encoding pode estar causando problemas")
            if "./" in caminho_codigo:
                causas.append("Caminho relativo pode não funcionar em todos os servidores")
        
        if not situacao_codigo.get("tratamento_erros", False):
            causas.append("Falta de tratamento de erros impede identificação do problema")
        
        if not situacao_codigo.get("feedback_visual", False):
            causas.append("Usuário não recebe feedback quando ocorre erro")
        
        return causas
    
    def _gerar_recomendacao(self, problema: str, causas: List[str]) -> str:
        """Gera recomendação baseada no problema"""
        if problema == "ARQUIVO PDF NÃO ENCONTRADO":
            return "Verificar se o arquivo 'curriculo de carlos costato.pdf' existe no diretório do projeto"
        
        if problema == "DESCOMPATIBILIDADE DE CAMINHO":
            return "Ajustar o caminho no código JavaScript para corresponder exatamente ao nome do arquivo"
        
        if problema == "ARQUIVO SEM PERMISSÃO DE ACESSO":
            return "Verificar permissões do arquivo PDF no servidor"
        
        if problema == "PROBLEMAS NO CÓDIGO JAVASCRIPT":
            return "Revisar e corrigir a função downloadCV() para tratamento adequado de erros"
        
        return "Realizar testes manuais no navegador para identificar o problema específico"

def main():
    analisador = AnalisadorProblemaDownload()
    analise = analisador.analisar_situacao_atual()
    
    print("\n" + "="*60)
    print("📋 RESUMO DA ANÁLISE")
    print("="*60)
    
    print(f"\n🎯 PROBLEMA IDENTIFICADO: {analise['problema_identificado']}")
    
    if analise['causas_possiveis']:
        print(f"\n🔍 CAUSAS POSSÍVEIS:")
        for i, causa in enumerate(analise['causas_possiveis'], 1):
            print(f"   {i}. {causa}")
    
    print(f"\n💡 RECOMENDAÇÃO: {analise['recomendacao']}")
    
    # Salvar análise
    with open('analise_problema_download.json', 'w', encoding='utf-8') as f:
        import json
        json.dump(analise, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n💾 Análise salva: analise_problema_download.json")
    
    # Perguntar sobre teste no navegador
    print(f"\n🌐 TESTE NO NAVEGADOR:")
    print(f"   1. Servidor local iniciado em: http://localhost:8000")
    print(f"   2. Acesse: http://localhost:8000/teste_download_manual.html")
    print(f"   3. Teste diferentes opções de download")
    print(f"   4. Verifique o console do navegador (F12) para erros")
    
    return analise

if __name__ == "__main__":
    main()
