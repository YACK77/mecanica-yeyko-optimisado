import os
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

SLACK_CHANNEL_URL = "https://app.slack.com/client/T0C9R799A4R/C0C9R7KBGTB"
SLACK_MENTOR_URL = "https://www.erasmoh.dev/es"

def get_slack_webhook():
    """Obtener URL del Webhook de Slack desde variables de entorno."""
    return os.getenv("SLACK_WEBHOOK_URL", "").strip()

import sys

def safe_print(msg: str):
    """Imprimir mensajes de consola de forma segura en Windows sin fallar por emojis."""
    try:
        print(msg)
    except UnicodeEncodeError:
        try:
            print(msg.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))
        except Exception:
            print(msg.encode("ascii", errors="ignore").decode("ascii"))

def send_slack_message(text: str, blocks: list = None) -> dict:
    """
    Enviar mensaje a Slack mediante Incoming Webhook.
    Si no hay webhook configurado, registra el evento en logs de forma segura sin romper el sistema.
    """
    webhook_url = get_slack_webhook()

    payload = {
        "text": text
    }
    if blocks:
        payload["blocks"] = blocks

    if not webhook_url:
        safe_print(f"[SLACK SIMULACIÓN] Notificación generada (Webhook no configurado):\n{text}")
        return {
            "status": "simulated",
            "message": "Slack Webhook no configurado en .env. El mensaje fue registrado en la consola del servidor.",
            "content": text
        }


    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            res_body = response.read().decode("utf-8")
            safe_print(f"[SLACK OK] Mensaje enviado a Slack con éxito: {res_body}")
            return {"status": "success", "message": "Notificación enviada a Slack con éxito"}
    except urllib.error.HTTPError as e:
        err_msg = f"HTTP Error {e.code}: {e.read().decode('utf-8')}"
        safe_print(f"[SLACK ERROR] {err_msg}")
        return {"status": "error", "message": err_msg}
    except Exception as e:
        err_msg = f"Error al enviar a Slack: {str(e)}"
        safe_print(f"[SLACK ERROR] {err_msg}")
        return {"status": "error", "message": err_msg}



def notify_sale(sale_id: int, cliente_nombre: str, placa: str, total: float, metodo_pago: str, items: list = None):
    """Notificar una venta concretada en el Punto de Venta."""
    placa_txt = f"`{placa}`" if placa else "*Sin placa*"
    detalle_items = ""
    if items:
        detalle_items = "\n".join([f"• {it.get('cantidad', 1)}x {it.get('nombre', 'Ítem')} - Bs {it.get('subtotal', 0):.2f}" for it in items[:5]])
        if len(items) > 5:
            detalle_items += f"\n• ... y {len(items) - 5} ítem(s) más"

    text = f"🚗💰 *¡Nueva Venta en Mecánica Yeyko!* (Venta #{sale_id})\n*Cliente:* {cliente_nombre}\n*Vehículo:* {placa_txt}\n*Total:* Bs {total:.2f}\n*Método:* {metodo_pago}"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🚗💰 Nueva Venta Registrada #{sale_id}",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Cliente:*\n{cliente_nombre}"},
                {"type": "mrkdwn", "text": f"*Vehículo / Placa:*\n{placa_txt}"},
                {"type": "mrkdwn", "text": f"*Total Cobrado:*\n*Bs {total:.2f}*"},
                {"type": "mrkdwn", "text": f"*Método de Pago:*\n{metodo_pago}"}
            ]
        }
    ]

    if detalle_items:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Detalle de Repuestos / Servicios:*\n{detalle_items}"
            }
        })

    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "🛠️ *Mecánica Yeyko* • Sistema de Control Operativo en Tiempo Real"
            }
        ]
    })

    return send_slack_message(text=text, blocks=blocks)


def notify_low_stock(producto_nombre: str, sku: str, stock_actual: int, stock_minimo: int):
    """Alerta roja de repuesto con existencia crítica o agotada."""
    urgencia = "🚨 *STOCK AGOTADO (0 unidades)*" if stock_actual <= 0 else f"⚠️ *STOCK CRÍTICO ({stock_actual} unidades)*"

    text = f"{urgencia} en Mecánica Yeyko: *{producto_nombre}* (SKU: `{sku}`). Mínimo requerido: {stock_minimo}."

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "⚠️ Alerta de Inventario Crítico",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Repuesto:*\n{producto_nombre}"},
                {"type": "mrkdwn", "text": f"*Código / SKU:*\n`{sku}`"},
                {"type": "mrkdwn", "text": f"*Existencia Actual:*\n*{stock_actual} unidades*"},
                {"type": "mrkdwn", "text": f"*Stock Mínimo:*\n{stock_minimo} unidades"}
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "📢 Se recomienda emitir una Orden de Compra al distribuidor a la brevedad."
                }
            ]
        }
    ]

    return send_slack_message(text=text, blocks=blocks)


def notify_purchase(purchase_id: int, proveedor: str, factura: str, total: float, items_count: int):
    """Notificar ingreso de compras al almacén."""
    factura_txt = f"`{factura}`" if factura else "*Sin factura*"
    text = f"📦📥 *Ingreso de Mercancía #{purchase_id}* de *{proveedor}*. Factura: {factura_txt}. Total: Bs {total:.2f}."

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"📦 Ingreso de Repuestos al Taller #{purchase_id}",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Proveedor:*\n{proveedor}"},
                {"type": "mrkdwn", "text": f"*N° Factura:*\n{factura_txt}"},
                {"type": "mrkdwn", "text": f"*Inversión:*\n*Bs {total:.2f}*"},
                {"type": "mrkdwn", "text": f"*Total Ítems:*\n{items_count} repuesto(s)"}
            ]
        }
    ]

    return send_slack_message(text=text, blocks=blocks)
