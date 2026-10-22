from database import SessionLocal
import models
from datetime import datetime, timezone

db = SessionLocal()

try:
    admin = db.query(models.User).filter(models.User.email == "admin@mecanicayeyko.com").first()
    filtro = db.query(models.Product).filter(models.Product.sku == "FLT-ACE-HILUX").first()
    aceite = db.query(models.Product).filter(models.Product.sku == "ACE-10W40-MOBIL").first()

    # 1. Crear una compra de prueba si no existe
    if db.query(models.Purchase).count() == 0 and filtro and aceite:
        compra = models.Purchase(
            proveedor_nombre="Distribuidora de Autopartes Santa Cruz S.R.L.",
            proveedor_nit="1028475021",
            numero_factura="FAC-00482",
            total_compra=350.00,
            usuario_id=admin.id if admin else None
        )
        db.add(compra)
        db.flush()

        it1 = models.PurchaseItem(
            purchase_id=compra.id,
            product_id=filtro.id,
            cantidad=5,
            costo_unitario=35.00,
            subtotal=175.00
        )
        it2 = models.PurchaseItem(
            purchase_id=compra.id,
            product_id=aceite.id,
            cantidad=1,
            costo_unitario=175.00,
            subtotal=175.00
        )
        db.add_all([it1, it2])
        print("[OK] Compra de prueba registrada con exito.")

    # 2. Crear una venta de prueba si no existe
    if db.query(models.Sale).count() == 0 and filtro and aceite:
        venta = models.Sale(
            cliente_nombre="Carlos Eduardo Mendez Rojas",
            cliente_ci_nit="5892341 SC",
            placa_vehiculo="3491-YKT",
            total_venta=250.00,
            metodo_pago="EFECTIVO",
            usuario_id=admin.id if admin else None
        )
        db.add(venta)
        db.flush()

        sv1 = models.SaleItem(
            sale_id=venta.id,
            product_id=filtro.id,
            cantidad=1,
            precio_unitario=60.00,
            subtotal=60.00
        )
        sv2 = models.SaleItem(
            sale_id=venta.id,
            product_id=aceite.id,
            cantidad=1,
            precio_unitario=190.00,
            subtotal=190.00
        )
        db.add_all([sv1, sv2])

        mov_salida = models.InventoryMovement(
            product_id=filtro.id,
            tipo_movimiento="SALIDA",
            cantidad=1,
            stock_anterior=filtro.stock_actual,
            stock_posterior=filtro.stock_actual - 1,
            referencia_origen=f"VENTA #{venta.id}",
            usuario_id=admin.id if admin else None,
            motivo="Cambio de aceite y filtro a vehiculo 3491-YKT"
        )
        filtro.stock_actual -= 1
        db.add(mov_salida)
        print("[OK] Venta de prueba registrada con exito.")

    db.commit()
    print("Todas las tablas pobladas!")
except Exception as e:
    db.rollback()
    print("Error:", e)
finally:
    db.close()
