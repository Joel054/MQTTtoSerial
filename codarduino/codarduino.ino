
int amarelo = 3;
int vermelho = 5;
int verde = 6;
int espera = 0;
char serial;

void setup() {
  pinMode(3, OUTPUT);
//  pinMode(5, OUTPUT);
//  pinMode(6, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin( 9600 );
}

void loop(){ 
  int leitura = analogRead(A0); //Armazena a leitura do pino A0 na variavel leitura
//  int pwm = map(leitura,0,1023,0,255);

  if (Serial.available() > 0) {
    // lê do buffer o dado recebido:
    serial = Serial.read();
    // responde com o dado recebido:
//    Serial.println(serial);
    if(serial == 'A'){
      digitalWrite(amarelo, HIGH);   // turn the LED on (HIGH is the voltage level)
    }
    if(serial == 'X'){
      digitalWrite(amarelo, LOW);
    }
    if(serial == 'M'){
      espera = 1000;
    }
    else{
      espera = serial;
    }
  }
  Serial.println(leitura);
  delay(espera);
}
