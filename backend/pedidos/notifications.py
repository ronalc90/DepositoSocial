import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings

def enviar_notificacion_pedido(pedido):
    """
    Envía notificación por email cuando se crea un pedido
    """
    try:
        cliente_email = pedido.get('cliente', {}).get('email', '')
        cliente_nombre = pedido.get('cliente', {}).get('nombre', '')
        pedido_id = pedido.get('_id', 'N/A')

        subject = f"Pedido Confirmado #{pedido_id} - Diana Margarita"

        items_html = ""
        for item in pedido.get('items', []):
            items_html += f"""
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{item.get('nombre')}</td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{item.get('cantidad')}</td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">${item.get('precio', 0):,.0f}</td>
            </tr>
            """

        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center;">
                <h1 style="color: white; margin: 0;">Diana Margarita</h1>
            </div>

            <div style="padding: 30px; background: #f8f9fa;">
                <h2 style="color: #333;">Hola {cliente_nombre},</h2>
                <p style="color: #666; font-size: 16px;">
                    Gracias por tu pedido. Hemos recibido tu solicitud y la procesaremos a la brevedad.
                </p>

                <div style="background: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #333; margin-top: 0;">Detalles del Pedido #{pedido_id}</h3>

                    <table style="width: 100%; border-collapse: collapse;">
                        <thead>
                            <tr style="background: #f8f9fa;">
                                <th style="padding: 10px; text-align: left;">Producto</th>
                                <th style="padding: 10px; text-align: left;">Cantidad</th>
                                <th style="padding: 10px; text-align: left;">Precio</th>
                            </tr>
                        </thead>
                        <tbody>
                            {items_html}
                        </tbody>
                    </table>

                    <div style="margin-top: 20px; padding-top: 20px; border-top: 2px solid #eee; text-align: right;">
                        <strong style="font-size: 18px;">Total: ${pedido.get('total', 0):,.0f} COP</strong>
                    </div>
                </div>

                <p style="color: #666;">
                    Estado: <strong>{pedido.get('estado', 'Pendiente')}</strong>
                </p>

                <p style="color: #999; font-size: 14px; margin-top: 30px;">
                    Si tienes alguna pregunta sobre tu pedido, no dudes en contactarnos.
                </p>
            </div>

            <div style="background: #333; padding: 20px; text-align: center; color: white;">
                <p style="margin: 0; font-size: 14px;">© 2025 Diana Margarita - Todos los derechos reservados</p>
            </div>
        </body>
        </html>
        """

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'noreply@dianamargarita.com'
        msg['To'] = cliente_email

        msg.attach(MIMEText(html, 'html'))

        print(f"[NOTIFICACIÓN] Email enviado a {cliente_email}")
        print(f"[NOTIFICACIÓN] Pedido #{pedido_id} - Total: ${pedido.get('total', 0):,.0f} COP")

        return True

    except Exception as e:
        print(f"Error enviando notificación: {e}")
        return False
