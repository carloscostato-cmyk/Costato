#!/usr/bin/env python3
"""
🔧 2 ESPECIALISTAS GIT - COMMIT E PUSH
Carlos Costato - Sistema de Controle de Versão
"""

import subprocess
import json
from datetime import datetime
from typing import Dict, List, Any
import os

class EspecialistaGit:
    """Especialista em operações Git com controle de qualidade"""
    
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        self.operacoes_realizadas = 0
        self.erros_corrigidos = 0
        self.branch_atual = ""
        self.status_repositorio = {}
        
    def verificar_status_repositorio(self) -> Dict[str, Any]:
        """Verifica status completo do repositório"""
        try:
            # Verificar se estamos em um repositório Git
            resultado = subprocess.run(
                ['git', 'status'],
                capture_output=True,
                text=True,
                cwd='c:\\Users\\Carlos Costato\\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\\Documents\\GitHub\\Costato'
            )
            
            if resultado.returncode != 0:
                return {"erro": "Não é um repositório Git", "status": "ERRO"}
            
            # Parse do status
            linhas = resultado.stdout.split('\n')
            branch_atual = ""
            arquivos_modificados = []
            arquivos_novos = []
            arquivos_nao_rastreados = []
            
            untracked_section = False
            
            for linha in linhas:
                if "On branch" in linha:
                    branch_atual = linha.replace("On branch", "").strip()
                elif "modified:" in linha:
                    # Extrair nome do arquivo após "modified:"
                    nome_arquivo = linha.replace("modified:", "").strip()
                    if nome_arquivo:
                        arquivos_modificados.append(nome_arquivo)
                elif "new file:" in linha:
                    # Extrair nome do arquivo após "new file:"
                    nome_arquivo = linha.replace("new file:", "").strip()
                    if nome_arquivo:
                        arquivos_novos.append(nome_arquivo)
                elif "Untracked files:" in linha:
                    untracked_section = True
                elif linha.startswith('\t') and untracked_section:
                    # Arquivos não rastreados começam com tab
                    nome_arquivo = linha.strip()
                    if nome_arquivo:
                        arquivos_nao_rastreados.append(nome_arquivo)
                elif linha.strip() and not linha.startswith('\t'):
                    untracked_section = False
            
            self.status_repositorio = {
                "branch_atual": branch_atual,
                "arquivos_modificados": arquivos_modificados,
                "arquivos_novos": arquivos_novos,
                "arquivos_nao_rastreados": arquivos_nao_rastreados,
                "status": "OK"
            }
            
            return self.status_repositorio
            
        except Exception as e:
            return {"erro": str(e), "status": "ERRO"}
    
    def validar_arquivos_para_commit(self) -> Dict[str, Any]:
        """Valida quais arquivos devem ser incluídos no commit"""
        status = self.verificar_status_repositorio()
        
        if status["status"] == "ERRO":
            return status
        
        arquivos_para_commit = []
        arquivos_ignorados = []
        
        # Arquivos modificados
        for arquivo in status["arquivos_modificados"]:
            if arquivo.endswith('.py') or arquivo.endswith('.html') or arquivo.endswith('.txt') or arquivo.endswith('.json'):
                arquivos_para_commit.append(arquivo)
            else:
                arquivos_ignorados.append(arquivo)
        
        # Arquivos novos
        for arquivo in status["arquivos_novos"]:
            if arquivo.endswith('.py') or arquivo.endswith('.html') or arquivo.endswith('.txt') or arquivo.endswith('.json'):
                arquivos_para_commit.append(arquivo)
            else:
                arquivos_ignorados.append(arquivo)
        
        # Arquivos não rastreados (relevantes)
        for arquivo in status["arquivos_nao_rastreados"]:
            if arquivo.endswith('.py') or arquivo.endswith('.html') or arquivo.endswith('.txt') or arquivo.endswith('.json'):
                arquivos_para_commit.append(arquivo)
            else:
                arquivos_ignorados.append(arquivo)
        
        return {
            "arquivos_para_commit": arquivos_para_commit,
            "arquivos_ignorados": arquivos_ignorados,
            "status": "OK"
        }
    
    def executar_commit(self, mensagem_commit: str) -> Dict[str, Any]:
        """Executa commit com validação"""
        try:
            # Validar arquivos
            validacao = self.validar_arquivos_para_commit()
            
            if validacao["status"] == "ERRO":
                return validacao
            
            # Adicionar arquivos ao staging
            for arquivo in validacao["arquivos_para_commit"]:
                resultado = subprocess.run(
                    ['git', 'add', arquivo],
                    capture_output=True,
                    text=True,
                    cwd='c:\\Users\\Carlos Costato\\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\\Documents\\GitHub\\Costato'
                )
                
                if resultado.returncode != 0:
                    return {"erro": f"Erro ao adicionar {arquivo}: {resultado.stderr}", "status": "ERRO"}
            
            # Executar commit
            resultado = subprocess.run(
                ['git', 'commit', '-m', mensagem_commit],
                capture_output=True,
                text=True,
                cwd='c:\\Users\\Carlos Costato\\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\\Documents\\GitHub\\Costato'
            )
            
            if resultado.returncode != 0:
                if "nothing to commit" in resultado.stdout:
                    return {"status": "NADA_A_COMMITAR", "mensagem": "Nenhuma alteração para commit"}
                else:
                    return {"erro": f"Erro no commit: {resultado.stderr}", "status": "ERRO"}
            
            self.operacoes_realizadas += 1
            
            return {
                "status": "SUCESSO",
                "mensagem": "Commit realizado com sucesso",
                "arquivos_commitados": validacao["arquivos_para_commit"],
                "arquivos_ignorados": validacao["arquivos_ignorados"]
            }
            
        except Exception as e:
            return {"erro": str(e), "status": "ERRO"}
    
    def executar_push(self, branch: str = None) -> Dict[str, Any]:
        """Executa push para repositório remoto"""
        try:
            # Verificar branch atual se não especificado
            if not branch:
                status = self.verificar_status_repositorio()
                if status["status"] == "ERRO":
                    return status
                branch = status["branch_atual"]
            
            # Executar push
            resultado = subprocess.run(
                ['git', 'push', 'origin', branch],
                capture_output=True,
                text=True,
                cwd='c:\\Users\\Carlos Costato\\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\\Documents\\GitHub\\Costato'
            )
            
            if resultado.returncode != 0:
                if "Everything up-to-date" in resultado.stdout:
                    return {"status": "ATUALIZADO", "mensagem": "Repositório já está atualizado"}
                else:
                    return {"erro": f"Erro no push: {resultado.stderr}", "status": "ERRO"}
            
            self.operacoes_realizadas += 1
            
            return {
                "status": "SUCESSO",
                "mensagem": f"Push realizado com sucesso para branch {branch}",
                "branch": branch
            }
            
        except Exception as e:
            return {"erro": str(e), "status": "ERRO"}

class EquipeEspecialistasGit:
    """Equipe de 2 Especialistas Git para Commit e Push"""
    
    def __init__(self):
        # 2 Especialistas Git
        self.especialista1 = EspecialistaGit(
            nome="Gabriel Silva",
            especialidade="Especialista em Controle de Versão e Qualidade de Código"
        )
        
        self.especialista2 = EspecialistaGit(
            nome="Mariana Costa",
            especialidade="Especialista em Operações Git e Deploy Seguro"
        )
        
        self.historico_operacoes = []
    
    def executar_commit_push_seguro(self) -> Dict[str, Any]:
        """Executa processo completo de commit e push com 2 especialistas"""
        print("EQUIPE DE ESPECIALISTAS GIT - COMMIT E PUSH")
        print("="*60)
        print(f"Especialista 1: {self.especialista1.nome}")
        print(f"Especialista 2: {self.especialista2.nome}")
        print("="*60)
        
        resultado_final = {
            "data_operacao": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "especialistas": [
                self.especialista1.nome,
                self.especialista2.nome
            ],
            "etapas": [],
            "status_final": "PENDENTE",
            "erros": []
        }
        
        try:
            # Etapa 1: Verificação do Especialista 1
            print(f"\n{self.especialista1.nome} - Verificando status do repositório...")
            status = self.especialista1.verificar_status_repositorio()
            
            if status["status"] == "ERRO":
                resultado_final["erros"].append(f"Erro na verificação: {status['erro']}")
                resultado_final["status_final"] = "ERRO"
                return resultado_final
            
            resultado_final["etapas"].append({
                "especialista": self.especialista1.nome,
                "etapa": "Verificação do Repositório",
                "status": "SUCESSO",
                "detalhes": status
            })
            
            print(f"   Branch: {status['branch_atual']}")
            print(f"   Arquivos modificados: {len(status['arquivos_modificados'])}")
            print(f"   Arquivos novos: {len(status['arquivos_novos'])}")
            print(f"   Arquivos nao rastreados: {len(status['arquivos_nao_rastreados'])}")
            
            # Etapa 2: Validação do Especialista 1
            print(f"\n{self.especialista1.nome} - Validando arquivos para commit...")
            validacao = self.especialista1.validar_arquivos_para_commit()
            
            if validacao["status"] == "ERRO":
                resultado_final["erros"].append(f"Erro na validação: {validacao['erro']}")
                resultado_final["status_final"] = "ERRO"
                return resultado_final
            
            resultado_final["etapas"].append({
                "especialista": self.especialista1.nome,
                "etapa": "Validação de Arquivos",
                "status": "SUCESSO",
                "detalhes": validacao
            })
            
            print(f"   Arquivos para commit: {len(validacao['arquivos_para_commit'])}")
            print(f"   Arquivos ignorados: {len(validacao['arquivos_ignorados'])}")
            
            # Etapa 3: Commit do Especialista 1
            if validacao["arquivos_para_commit"]:
                mensagem_commit = "feat: Adicionar botão download CV no box do robô com 3 agentes de qualidade\n\n- Implementar botão de download do currículo PDF\n- Adicionar 3 agentes de qualidade para validação e execução\n- Manter funcionalidade existente do robô leitor\n- Design responsivo e feedback visual\n- Tratamento de erros robusto"
                
                print(f"\n{self.especialista1.nome} - Executando commit...")
                commit_result = self.especialista1.executar_commit(mensagem_commit)
                
                resultado_final["etapas"].append({
                    "especialista": self.especialista1.nome,
                    "etapa": "Commit",
                    "status": commit_result["status"],
                    "detalhes": commit_result
                })
                
                if commit_result["status"] == "SUCESSO":
                    print(f"   {commit_result['mensagem']}")
                    print(f"   Arquivos commitados: {len(commit_result['arquivos_commitados'])}")
                elif commit_result["status"] == "NADA_A_COMMITAR":
                    print(f"   {commit_result['mensagem']}")
                else:
                    resultado_final["erros"].append(f"Erro no commit: {commit_result.get('erro', 'Erro desconhecido')}")
                    resultado_final["status_final"] = "ERRO"
                    return resultado_final
            else:
                print(f"\nNenhum arquivo para commit")
                resultado_final["etapas"].append({
                    "especialista": self.especialista1.nome,
                    "etapa": "Commit",
                    "status": "NADA_A_COMMITAR",
                    "detalhes": "Nenhuma alteração para commit"
                })
            
            # Etapa 4: Push do Especialista 2
            print(f"\n{self.especialista2.nome} - Executando push...")
            push_result = self.especialista2.executar_push()
            
            resultado_final["etapas"].append({
                "especialista": self.especialista2.nome,
                "etapa": "Push",
                "status": push_result["status"],
                "detalhes": push_result
            })
            
            if push_result["status"] == "SUCESSO":
                print(f"   {push_result['mensagem']}")
                resultado_final["status_final"] = "SUCESSO"
            elif push_result["status"] == "ATUALIZADO":
                print(f"   {push_result['mensagem']}")
                resultado_final["status_final"] = "ATUALIZADO"
            else:
                resultado_final["erros"].append(f"Erro no push: {push_result.get('erro', 'Erro desconhecido')}")
                resultado_final["status_final"] = "ERRO"
            
            # Salvar histórico
            self.historico_operacoes.append(resultado_final)
            self._salvar_historico()
            
        except Exception as e:
            resultado_final["erros"].append(f"Erro geral: {str(e)}")
            resultado_final["status_final"] = "ERRO"
        
        return resultado_final
    
    def _salvar_historico(self):
        """Salva histórico das operações"""
        try:
            with open('historico-git-operacoes.json', 'w', encoding='utf-8') as f:
                json.dump(self.historico_operacoes, f, ensure_ascii=False, indent=2, default=str)
            print(f"\nHistorico salvo: historico-git-operacoes.json")
        except Exception as e:
            print(f"\nErro ao salvar historico: {e}")
    
    def gerar_relatorio_operacao(self) -> str:
        """Gera relatório da operação"""
        resultado = self.executar_commit_push_seguro()
        
        relatorio = f"""
RELATORIO DE OPERACAO GIT - COMMIT E PUSH
{'='*60}

Data: {resultado['data_operacao']}
Especialistas: {', '.join(resultado['especialistas'])}
Status Final: {resultado['status_final']}

ETAPAS EXECUTADAS:
"""
        
        for i, etapa in enumerate(resultado['etapas'], 1):
            relatorio += f"""
{i}. {etapa['especialista']} - {etapa['etapa']}
   Status: {etapa['status']}
"""
            if etapa['status'] == 'SUCESSO':
                if 'arquivos_commitados' in etapa['detalhes']:
                    relatorio += f"   Arquivos: {len(etapa['detalhes']['arquivos_commitados'])}\n"
                elif 'branch' in etapa['detalhes']:
                    relatorio += f"   Branch: {etapa['detalhes']['branch']}\n"
            elif etapa['status'] == 'ERRO':
                relatorio += f"   Erro: {etapa['detalhes'].get('erro', 'Erro desconhecido')}\n"
        
        if resultado['erros']:
            relatorio += f"""
ERROS ENCONTRADOS:
"""
            for erro in resultado['erros']:
                relatorio += f"• {erro}\n"
        
        relatorio += f"""
ESTATISTICAS:
• Operacoes Especialista 1: {self.especialista1.operacoes_realizadas}
• Operacoes Especialista 2: {self.especialista2.operacoes_realizadas}
• Total de Erros Corrigidos: {self.especialista1.erros_corrigidos + self.especialista2.erros_corrigidos}

CONCLUSAO:
Operacao {'concluida com sucesso' if resultado['status_final'] in ['SUCESSO', 'ATUALIZADO'] else 'finalizada com erros'}.

---
Relatorio gerado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Sistema: Equipe de Especialistas Git v1.0
"""
        
        # Salvar relatório
        with open('relatorio-git-operacao.txt', 'w', encoding='utf-8') as f:
            f.write(relatorio)
        
        print(f"\nRelatorio salvo: relatorio-git-operacao.txt")
        
        return relatorio

# Executar operação Git
if __name__ == "__main__":
    equipe = EquipeEspecialistasGit()
    
    print("EQUIPE DE 2 ESPECIALISTAS GIT - COMMIT E PUSH")
    print("="*60)
    print("Carlos Costato - Sistema de Controle de Versão")
    print("="*60)
    
    # Executar operação completa
    relatorio = equipe.gerar_relatorio_operacao()
    
    print(f"\nOPERACAO CONCLUIDA!")
    print(f"Relatorio completo: relatorio-git-operacao.txt")
    print(f"Historico de operacoes: historico-git-operacoes.json")
    print(f"Verifique o repositorio remoto para confirmar as alteracoes")
