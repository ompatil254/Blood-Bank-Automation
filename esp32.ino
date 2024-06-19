#include <SPI.h>
#include <MFRC522.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HTTPClient.h>

#define SS_PIN 21
#define RST_PIN 22
MFRC522 mfrc522(SS_PIN, RST_PIN); 

#define WIFI_NETWORK "Skyworth"
#define WIFI_PASSWORD "628717806"
#define WIFI_TIMEOUT_MS 20000

#define serverName "http://{YOUR_WIFI_IPV4}:8000/rfid_val/" //check seetings.py of RFID_Blood_Bank for more information

// int sensorPin = A0;
// int sensorValue = 0;
// String lastBlock="";

void sendData(String rfid_id) {
  HTTPClient http;
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");
  String jsonData = "{\"RFID\": \"" + rfid_id + "\"}";
  int httpCode = http.POST(jsonData);
  Serial.println(httpCode);
  http.end();
}

void connectToWiFi() {
  Serial.print("connecting to WiFi");
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_NETWORK, WIFI_PASSWORD);

  unsigned long startAttemptTime = millis();

  while(WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < WIFI_TIMEOUT_MS) {
    Serial.print(".");
    delay(100);
  }

  if(WiFi.status() != WL_CONNECTED) {
    Serial.print(" Failed!");
  }

  else {
    Serial.print("Connected!");
    Serial.println(WiFi.localIP());
  }
}

void setup() {
  Serial.begin(9600);
  SPI.begin();       
  mfrc522.PCD_Init();
  connectToWiFi();
//mfrc522.setPassiveActivationRetries(0x9A);
}

boolean flag=false;
String rfid;
// int counter=0;

void loop() {
  if ( !mfrc522.PICC_IsNewCardPresent()) {
    if(mfrc522.PICC_IsNewCardPresent()){
      if(!flag){
        // byte sector         = 1;
        // byte blockAddr      = 4;
        // byte dataBlock[]    = {
        //     0x01, 0x02, 0x03, 0x04, //  1,  2,   3,  4,
        //     0x05, 0x06, 0x07, 0x08, //  5,  6,   7,  8,
        //     0x08, 0x09, 0xff, 0x0b, //  9, 10, 255, 12,
        //     0x0c, 0x0d, 0x0e, 0x0f  // 13, 14,  15, 16
        // };

        // byte trailerBlock   = 7;
        // byte status;
        // byte buffer[18];
        // byte size = sizeof(buffer);
        // status = mfrc522.MIFARE_Read(blockAddr, buffer, &size);
        // dump_byte_array(buffer, 16);
        // dump_byte_array(); 
        Serial.println("Card detected");
        mfrc522.PICC_ReadCardSerial();
        rfid = array_to_string(mfrc522.uid.uidByte, 4);
        String rfid_id = "1" + rfid;
        sendData(rfid_id);
        flag=true;
      }
    }
    else{
      if(flag){
        Serial.println("Card removed");
        String rfid_id = "0" + rfid;
        sendData(rfid_id);
        flag=false;
      }
    }
  return;
  }  
}

String array_to_string(byte array[], unsigned int len)
{
  char buffer[32] = "";
   for (unsigned int i = 0; i < len; i++)
   {
      byte nib1 = (array[i] >> 4) & 0x0F;
      byte nib2 = (array[i] >> 0) & 0x0F;
      buffer[i*2+0] = nib1  < 0xA ? '0' + nib1  : 'A' + nib1  - 0xA;
      buffer[i*2+1] = nib2  < 0xA ? '0' + nib2  : 'A' + nib2  - 0xA;
   }
   buffer[len*2] = '\0';
   String rfid = buffer;
   return rfid;
}

// byte *buffer, byte bufferSize
// void dump_byte_array() {
// String a=String((char)buffer[9]);
// String b=String((char)buffer[10]);
// String c=String((char)buffer[11]);
// String d=String((char)buffer[12]);
// String str="";
// str+=a;
// str+=b;
// str+=c;
// str+=d;
// lastBlock=str;
// Serial.println("Card detected");
// }