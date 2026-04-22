"""
Módulo de notificação via Telegram Bot.
Responsável por enviar relatórios e alertas de vagas ao Carlos Costato.
"""

import os
import json
import requests
from datetime import datetime


class TelegramNotifier:
    def __init__(self):
        self.bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def _send(self, message: str, parse_mode: str = "HTML") -> bool:
        """Envia uma mensagem via Telegram Bot API."""
        if not self.bot_token or not self.chat_id:
            print("❌ ERRO: TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID não configurados.")
            print("   Acesse: GitHub repo → Settings → Secrets and variables → Actions")
            return False

        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": parse_mode,
        }
        try:
            response = requests.post(self.api_url, json=payload, timeout=10)
            response.raise_for_status()
            print(f"✅ Mensagem enviada ao Telegram com sucesso!")
            return True
        except requests.exceptions.RequestException as e:
            print(f"❌ Falha ao enviar mensagem para o Telegram: {e}")
            return False

    def send_job_report(self, jobs: list, session_label: str = "Relatório"):
        """Envia um relatório formatado de vagas encontradas."""
        now = datetime.now().strftime("%d/%m/%Y %H:%M")

        if not jobs:
            message = (
                f"🤖 <b>Agente de Carreira | {session_label}</b>\n"
                f"🕐 {now} (Horário de Brasília)\n\n"
                f"🔍 Varredura concluída.\n"
                f"📭 Nenhuma vaga nova encontrada neste ciclo.\n\n"
                f"<i>Próxima verificação em breve...</i>"
            )
        else:
            lines = [
                f"🤖 <b>Agente de Carreira | {session_label}</b>",
                f"🕐 {now} (Horário de Brasília)",
                f"",
                f"🎯 <b>{len(jobs)} vaga(s) encontrada(s) para você:</b>",
                "",
            ]
            for i, job in enumerate(jobs[:8], 1):  # Máx 8 vagas por mensagem
                score_emoji = "🔥" if job.get("match_score", 0) > 60 else "⭐"
                lines.append(
                    f"{score_emoji} <b>{i}. {job.get('title', 'N/A')}</b>\n"
                    f"   🏢 {job.get('company', 'N/A')}\n"
                    f"   📊 Match: {job.get('match_score', 0)}%\n"
                    f"   🔗 <a href=\"{job.get('url', '#')}\">Ver Vaga</a>\n"
                )
            lines.append("")
            lines.append(f"<i>Continue brilhando, Carlos! 🚀</i>")
            message = "\n".join(lines)

        self._send(message)

    def send_error_alert(self, error_msg: str):
        """Envia alerta de erro para o Telegram."""
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        message = (
            f"⚠️ <b>Agente de Carreira | ALERTA DE ERRO</b>\n"
            f"🕐 {now}\n\n"
            f"<code>{error_msg[:500]}</code>\n\n"
            f"<i>Verifique o GitHub Actions para mais detalhes.</i>"
        )
        self._send(message)


if __name__ == "__main__":
    # Teste local (requer variáveis de ambiente configuradas)
    notifier = TelegramNotifier()
    notifier.send_job_report(
        jobs=[
            {
                "title": "Senior IT Project Manager",
                "company": "ACME Corp",
                "match_score": 85,
                "url": "https://example.com/vaga",
            }
        ],
        session_label="Teste Local",
    )
