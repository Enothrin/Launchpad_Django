// A sound file object
var song;
var tempX=20;
var tempY=1;
	var active=false;
	var count = 5;
function preload() {
  // Load a sound file
  song = loadSound('/static/accounts/css/sound.mp3');
}

function setup() {
  createCanvas(500, 300);
  background(300);
  // Loop the sound forever
  // (well, at least until stop() is called)
  song.loop();
}

function draw() {


  // Set the volume to a range between 0 and 1.0
  var volume = map(250, tempY, width , 0, 1);
  volume = constrain(volume, 0, 1);
  song.amp(volume);
  if(frameCount%60 == 0) {}

  if ((tempY < 247)&&(!active)){tempY=tempY+8;}

  if (active){tempY=tempY-4;count=count-1;}
    if(!active&&int(volume*200)==1)
    {tempY=248;song.amp(0);}
  if (count<0){active=false;}

   if (mouseIsPressed){
       tempX=mouseX;
       active=true;
       count=5;
   }
       background(300);
       stroke(0);
       fill(51, 100);
       rect(tempX, tempY, 4, 50);
       textSize(30);
       text(int(volume*199), 10+tempX, 35+tempY);

  // Draw some circles to show what is going on

}


