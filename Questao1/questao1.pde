  float p2x = 150;
  float p2y = 400;
  float p3x = 250;
  float p3y = 200;

void setup(){
  size(800,600);
}

void draw(){
  background(128);
  float p1x = 100;
  float p1y = 100;
  float p4x = 700;
  float p4y = 100;
  char aux = 'a';
  
  beginShape();
  vertex(p1x, p1y);
  if (mousePressed && (mouseButton == RIGHT)){
    aux = 'a';

  }else if (mousePressed && (mouseButton == LEFT)){
    aux = 'b';

  }
  
  if (aux == 'a'){
    p2x = mouseX;
    p2y = mouseY;
  }else if (aux == 'b'){
    p3x = mouseX;
    p3y = mouseY;
  }
    
  for(float t = 0; t <= 1; t += 0.01){
    float ax = p1x + t*(p2x-p1x);
    float ay = p1y + t*(p2y-p1y);
    float bx = p2x + t*(p3x-p2x);
    float by = p2y + t*(p3y-p2y);
    float cx = p3x + t*(p4x-p3x);
    float cy = p3y + t*(p4y-p3y);
    float dx = ax + t*(bx-ax);
    float dy = ay + t*(by-ay);
    float ex = bx + t*(cx-bx);
    float ey = by + t*(cy-by);
    float fx = dx + t*(ex-dx);
    float fy = dy + t*(ey-dy);
    vertex(fx,fy);  
    
  }
  vertex(p4x, p4y);
  

  
  endShape(CLOSE);
}
