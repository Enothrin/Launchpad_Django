// A sound file object
var song;
var tempX=50;
var tempY=1;
var active=false;
var count = 5;
var GRAVITY = 1;



// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;

      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
          height: '90',
          width: '160',
          videoId: 'xo74Dn7W_pA',
          playerVars: {'modestbranding':1, 'autoplay': 1, 'controls': 0, 'showinfo':0  ,'iv_load_policy':3,},
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
      }



function setup() {
  createCanvas(500, 300);
  background(300);
  bar = createSprite(50,40);

  ground = createSprite(100,324,50 ,50);
  ground2 = createSprite(150,274,50 ,50);
  ground3 = createSprite(200,224,50 ,50);
  ground4 = createSprite(250,174,50 ,50);
  ground5 = createSprite(300,124,50 ,50);

  ground.shapeColor =  color((25),(25),(255));
  ground2.shapeColor = color((25),(25),(255));
  ground3.shapeColor = color((25),(25),(255));
  ground4.shapeColor = color((25),(25),(255));
  ground5.shapeColor = color((25),(25),(255));

}

function draw() {
    bar.position.x=tempX;
    bar.velocity.y += GRAVITY;
      if((bar.collide(ground)) || (bar.collide(ground2)) || (bar.collide(ground3)) || (bar.collide(ground4))|| (bar.collide(ground5))) {
          bar.velocity.y = 0;
      }

  // Set the volume to a range between 0 and 1.0
  var volume = map(250, bar.position.y, width , 0, 1);
  volume = constrain(volume, 0, 1);

  try {player.setVolume(volume*100)} catch(err) {}


  if(frameCount%60 == 0) {}

  if ((tempY < 247)&&(!active)){tempY=tempY+8;}

  if (active){tempY=tempY-4;count=count-1;}
    if(!active&&int(volume*200)==1)
    {tempY=248;try {player.setVolume(volume*100)} catch(err) {}}
  if (count<0){active=false;}

    if (mouseIsPressed){
        tempX=mouseX;
        active=true;
        count=5;
        bar.velocity.y = -4;
    }

    background(300);
    stroke(0);
    fill(51, 100);
    textSize(30);
    text(int(volume*199), bar.position.x+70, bar.position.y-4);

    drawSprites();
}


