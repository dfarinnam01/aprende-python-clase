import cv2

# DATOS DE LA CÁMARA
usuario = "bmxavierm01"
password = "Badajoz.2024"
ip = "192.168.60.56"   # IP de tu cámara
puerto = "554"

# URL RTSP
rtsp_url = f"rtsp://{usuario}:{password}@{ip}:{puerto}/stream1"

print("Conectando a la cámara...")
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("❌ No se pudo conectar a la cámara")
    exit()

print("✅ Cámara conectada (pulsa Q para salir)")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ No se pudo obtener imagen")
        break

    cv2.imshow("Tapo C210 - En directo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()