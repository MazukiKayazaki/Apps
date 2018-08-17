#include <SDL.h>
#include <iostream>
#include <string.h>
#include <SDL_image.h>
#include <SDL_ttf.h>
#include <SDL_mixer.h>


#define SCREEN_WIDTH 720
#define SCREEN_HEIGHT 600

#define MAIN_VIEWPORT_WIDTH 720
#define MAIN_VIEWPORT_HEIGHT 450

#define SECONDARY_VIEWPORT_WIDTH 720
#define SECONDARY_VIEWPORT_HEIGHT 150

//prototypes
bool init();
bool loadMedia();
void close();


class LTexture {
    public:
        //Intitializes variables
        LTexture(); //Constructeur

        //
        ~LTexture(); //Destructeur

        bool loadFromFile( std::string path);


        bool loadFromRenderedText ( std::string textureText, SDL_Color textColor);
        //Deallocates texture
        void free();

        //Renders texture at given point
        void renderOutlinedCentered();
        void render( int x, int y);
        void renderCentered();

        //Gets image dimensions.
        int getWidth();
        int getHeight();

        //Set blending
        void setBlendMode(SDL_BlendMode blending);
        void setAlpha(Uint8 alpha);

    private:

        //The actual hardware texture
        SDL_Texture* mTexture;

        //Image dimensions
        int mWidth;
        int mHeight;

};

//the window we'll be rendering to
SDL_Window* gWindow = NULL;

//The window renderer
SDL_Renderer* gRenderer = NULL;


// the music that will be played
Mix_Music* gMusicIntro = NULL;



TTF_Font *gFont = NULL;

int gCurrentTexture ;
LTexture gTextures[10];
char gTexturesPath[10][100] = {  "images/image1.png",
                            "images/image2.png",
                            "images/image3.png",
                            "images/image4.png",
                            "images/image5.png",
                            "images/image6.png",
                            "images/image7.png",
                            "images/image8.png",
                            "images/image9.png",
                            "images/image10.png"};


LTexture gTexts[10];
char gTextsPath[10][100] = {
                            "texts/text1.png",
                            "texts/text2.png",
                            "texts/text3.png",
                            "texts/text4.png",
                            "texts/text5.png",
                            "texts/text6.png",
                            "texts/text7.png",
                            "texts/text8.png",
                            "texts/text9.png",
                            "texts/text10.png"
                            };


LTexture gClockFrames[11];
char gClockFramesPath[11][100] = {
                            "GUI/clock_00.png",
                             "GUI/clock_01.png",
                              "GUI/clock_02.png",
                               "GUI/clock_03.png",
                                "GUI/clock_04.png",
                                 "GUI/clock_05.png",
                                  "GUI/clock_06.png",
                                   "GUI/clock_07.png",
                                    "GUI/clock_08.png",
                                     "GUI/clock_09.png",
                                      "GUI/clock_10.png"};

LTexture gIntroFrames[10];
char gIntroFramesPath[10][100] =  {
    "GUI/introFrame1.png",
    "GUI/introFrame2.png",
    "GUI/introFrame3.png",
    "GUI/introFrame4.png",
    "GUI/introFrame5.png",
    "GUI/introFrame6.png",
    "GUI/introFrame7.png",
    "GUI/introFrame8.png",
    "GUI/introFrame9.png",
    "GUI/introFrame10.png"


};


LTexture gCorrectAnswerText;
LTexture gWrongAnswerText;
LTexture gPressEnterText;

LTexture gScoreBoard100;
LTexture gScoreBoard70;
LTexture gScoreBoard50;
LTexture gScoreBoard;

LTexture gTimeText;
LTexture gMarkText;
LTexture gLevelText;
LTexture gAccuracyText;
LTexture gScoreText;

LTexture gMidoriyaFullBody;

LTexture gArrow;

LTexture glevelSelectionBoku;
LTexture glockIcon;



//Scene Textures
LTexture gTexture1;
LTexture gBackground;








LTexture::LTexture()
{
    //Intialize
    mTexture = NULL;
    mWidth =  0;
    mHeight = 0;
}

LTexture::~LTexture()
{
    //Deallocate
    free();
}

bool LTexture::loadFromFile(std::string path)
{
    //Get rid of preexisting texture
    free();
    //the final texture
    SDL_Texture* newTexture = NULL;
    //Load the image at a specified path
    SDL_Surface* loadedSurface = IMG_Load(path.c_str());
    if (loadedSurface == NULL)
    {
        printf("Unable to load image %s! SDL_image Error: %s\n",path.c_str(),IMG_GetError());
    }
    else
    {
        //ColorKey Image ( no need)
        SDL_SetColorKey( loadedSurface, SDL_TRUE, SDL_MapRGB(loadedSurface->format,0 ,255,255));

        newTexture = SDL_CreateTextureFromSurface(gRenderer,loadedSurface);
        if (newTexture == NULL )
        {
            printf("Unable to create the texture from %s! SDL_image Error: %s\n",path.c_str(),SDL_GetError());
        }
        else
        {
            mWidth = loadedSurface->w;
            mHeight = loadedSurface->h;
        }
        SDL_FreeSurface(loadedSurface);
    }

    mTexture = newTexture;
    return mTexture != NULL;
}

bool LTexture::loadFromRenderedText(std::string textureText, SDL_Color textColor)
{
    free();
    SDL_Surface* textSurface = TTF_RenderText_Solid( gFont, textureText.c_str(), textColor );
    if ( textSurface == NULL)
    {
        printf("Unable to render text surface! SDL_ttf Error: %s\n",TTF_GetError());

    }
    else
    {
        mTexture = SDL_CreateTextureFromSurface(gRenderer, textSurface );
        if (mTexture == NULL)
        {
            printf( "Unable to create texture from rendered text! SDL Error: %s\n", SDL_GetError() );
        }
        else
        {
            mWidth = textSurface->w;
            mHeight = textSurface->h;

        }
        SDL_FreeSurface( textSurface );
    }

     return mTexture != NULL;
}




void LTexture::free()
{
    //Free texture if it exists
    if ( mTexture != NULL )
    {
        SDL_DestroyTexture(mTexture);
        mTexture = NULL;
        mWidth = 0;
        mHeight = 0;
    }
}

void LTexture:: render(int x, int y)
{
    //Set Rendering space and render to screen
    SDL_Rect renderQuad = { x, y, mWidth, mHeight};
    SDL_RenderCopy(gRenderer, mTexture, NULL,&renderQuad);
}

void LTexture::renderOutlinedCentered()
{
    //Set Rendering space and render to screen
    SDL_Rect renderQuad = { (MAIN_VIEWPORT_WIDTH-mWidth)/2, (MAIN_VIEWPORT_HEIGHT-mHeight)/2, mWidth, mHeight};
    SDL_Rect outlineQuad = { (MAIN_VIEWPORT_WIDTH-mWidth)/2-5, (MAIN_VIEWPORT_HEIGHT-mHeight)/2-5, mWidth+10, mHeight+10};
    SDL_SetRenderDrawColor(gRenderer, 255,0,0,255);
    SDL_RenderFillRect(gRenderer,&outlineQuad);

    SDL_RenderCopy(gRenderer, mTexture, NULL,&renderQuad);
}



void LTexture::renderCentered()
{
    SDL_Rect renderQuad = { (MAIN_VIEWPORT_WIDTH-mWidth)/2, (MAIN_VIEWPORT_HEIGHT-mHeight)/2, mWidth, mHeight};

    SDL_RenderCopy(gRenderer, mTexture, NULL,&renderQuad);
}




int LTexture::getWidth()
{
    return mWidth;
}

int LTexture::getHeight()
{
    return mHeight;
}

void LTexture::setBlendMode(SDL_BlendMode blending)
{
    SDL_SetTextureBlendMode(mTexture,blending);
}

void LTexture::setAlpha(Uint8 alpha)
{
    SDL_SetTextureAlphaMod(mTexture, alpha);
}


bool init()
{
    bool success = true;
    if ( SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO) <0 )
    {
        printf("Failed to initiliaze SDL! SDL Error: %s\n",SDL_GetError());
        success = false;
    }
    else
    {
        gWindow = SDL_CreateWindow("My hero Academia !", SDL_WINDOWPOS_UNDEFINED ,SDL_WINDOWPOS_UNDEFINED , SCREEN_WIDTH ,SCREEN_HEIGHT, SDL_WINDOW_SHOWN );
        if (gWindow == NULL)
        {
            printf("Failed to create a window! SDL Error : %s\n",SDL_GetError());
            success = false;
        }
        else
        {

            gRenderer = SDL_CreateRenderer(gWindow,-1 ,SDL_RENDERER_ACCELERATED);

            if (gRenderer == NULL)
            {
                printf("Failed to create a renderer! SDL Error: %s\n", SDL_GetError());
                success = false;
            }
            else
            {
                int imgFlags = IMG_INIT_PNG;
                if (!(IMG_Init(imgFlags)& imgFlags ))
                {
                    printf("Failed to initiliaze SDL_image! SDL_image Error: %s\n",IMG_GetError());
                    success = false;
                }

                if ( TTF_Init() == -1)
                {
                    printf("SDL_ttf could not initialize! SDL_ttf Error: %s\n", TTF_GetError());
                    success = false;
                }



                /*if ( Mix_OpenAudio(22050, AUDIO_S16SYS, 2, 640) < 0 )
                    printf( "SDL_mixer could not initialize! SDL_mixer Error: %s\n", SDL_GetError() );
                    success = false;*/
            }

        }
    }
    return success;
}

bool loadMedia()
{
   bool success = true;

   for ( int i = 0 ; i< 10 ; i++)
   {
        if ( !gTextures[i].loadFromFile(gTexturesPath[i]))
        {
            printf("Failed to load %s texture image!\n",gTexturesPath[i]);
            success = false;
        }
   }

    for ( int i = 0 ; i< 10 ; i++)
   {
        if ( !gTexts[i].loadFromFile(gTextsPath[i]))
        {
            printf("Failed to load %s texture image!\n",gTextsPath[i]);
            success = false;
        }
   }

    for ( int i = 0 ; i< 11 ; i++)
   {
        if ( !gClockFrames[i].loadFromFile(gClockFramesPath[i]))
        {
            printf("Failed to load %s texture image!\n",gClockFramesPath[i]);
            success = false;
        }
   }
    for ( int i = 0 ; i< 10 ; i++)
   {
        if ( !gIntroFrames[i].loadFromFile(gIntroFramesPath[i]))
        {
            printf("Failed to load %s texture image!\n",gIntroFramesPath[i]);
            success = false;
        }
        else
        {
            gIntroFrames[i].setBlendMode(SDL_BLENDMODE_BLEND);
        }
   }



    if ( !gArrow.loadFromFile("GUI/arrow.png"))
   {
       printf("Failed to load BACKGROUND's texture image!\n");
       success = false;
   }
    if ( !gCorrectAnswerText.loadFromFile("GUI/Correct_answer.png"))
   {
       printf("Failed to load Correct_answer's texture image!\n");
       success = false;
   }
    if ( !gWrongAnswerText.loadFromFile("GUI/Wrong_answer.png"))
   {
       printf("Failed to load Wrong_answer's texture image!\n");
       success = false;
   }
    if ( !gPressEnterText.loadFromFile("GUI/Press_Enter.png"))
   {
       printf("Failed to load Press_enter's texture image!\n");
       success = false;
   }
    if ( !gMidoriyaFullBody.loadFromFile("images/midoriya_full_body.png"))
   {
       printf("Failed to load Correct_answer's texture image!\n");
       success = false;
   }
   if ( !gScoreBoard.loadFromFile("GUI/scoreBoard.png"))
   {
       printf("Failed to load scoreBoard's texture image!\n");
       success = false;
   }
   if ( !gScoreBoard100.loadFromFile("GUI/scoreBoard100.png"))
   {
       printf("Failed to load scoreBoard's texture image!\n");
       success = false;
   }
   if ( !gScoreBoard70.loadFromFile("GUI/scoreBoard70.png"))
   {
       printf("Failed to load scoreBoard's texture image!\n");
       success = false;
   }
   if ( !gScoreBoard50.loadFromFile("GUI/scoreBoard50.png"))
   {
       printf("Failed to load scoreBoard's texture image!\n");
       success = false;
   }



   if ( !glevelSelectionBoku.loadFromFile("GUI/level_selection_bokunohero.png"))
   {
       printf("Failed to load level selection.");
       success = false;
   }
    if ( !glockIcon.loadFromFile("GUI/locked_icon.png"))
   {
       printf("Failed to load locked_icon.png.");
       success = false;
   }







   gFont = TTF_OpenFont("fonts/Consola.ttf",24);
   if( gFont == NULL )
   {
        printf( "Failed to load lazy font! SDL_ttf Error: %s\n", TTF_GetError() );
        success = false;
   }
   else
   {
       SDL_Color textColor = { 255, 0, 0 };
       char text[20];
       itoa(5,text,10);
       if( !gTimeText.loadFromRenderedText( text , textColor ) )
       {
            printf( "Failed to render text texture!\n" );
            success = false;
       }





   }


    // load MUSIC HERE
    /*gMusicIntro = Mix_LoadMUS("music/BokuNoHeroAcademiaIntro.wav");
    if (gMusicIntro == NULL)
    {
        printf("Failed to load beat music! SDL_mixerError: %s\n",Mix_GetError() );
        success = false;
    }
    */



   //Load Foo's texture
   /*if ( !gTexture1.loadFromFile("images/image4.png"))
   {
       printf("Failed to load image4's texture image!\n");
       success = false;
   }*/

    if ( !gBackground.loadFromFile("images/BACKGROUND.png"))
   {
       printf("Failed to load BACKGROUND's texture image!\n");
       success = false;
   }
   else
   {
       gBackground.setBlendMode(SDL_BLENDMODE_BLEND);
   }



    return success;
}

void close()
{
    //Free loaded images

    for ( int i = 0 ; i< 10 ; i++)
   {
        gTextures[i].free();
   }

    for ( int i = 0 ; i< 10 ; i++)
   {
        gTexts[i].free();
   }


    for ( int i = 0 ; i< 11 ; i++)
   {
        gClockFrames[i].free();
   }

   gArrow.free();
   gCorrectAnswerText.free();
   gWrongAnswerText.free();
   gPressEnterText.free();
   gPressEnterText.free();
   gMidoriyaFullBody.free();
   gScoreBoard.free();

    //Destroy Window
    SDL_DestroyRenderer(gRenderer);
    SDL_DestroyWindow(gWindow);
    gRenderer = NULL;
    gWindow = NULL;

    //Close music
    Mix_FreeMusic( gMusicIntro );
    gMusicIntro = NULL;


    TTF_CloseFont( gFont ); gFont = NULL;

    TTF_Quit();
    IMG_Quit();
    SDL_Quit();
}

int main(int argc,char* argv[])
{
    if (!init())
    {
        printf("Unable to initialize SDL! SDL_Error: %s\n",SDL_GetError());
    }

    if (!loadMedia())
    {
        printf("Unable to load media!");
    }

    if (Mix_OpenAudio(22050, AUDIO_S16SYS, 2, 640) < 0)
    {
        printf("failed to open Audio");
    }

    Mix_Music* gMusicIntro = Mix_LoadMUS("music/BokuNoHeroAcademiaIntro.wav");
    if ( gMusicIntro == NULL)
    {
        printf("damn %s", Mix_GetError());
    }

    bool quit = false;
    SDL_Event e;
    int a = 125;
    int gIntroFramesAlpha[10] = {255,255,255,255,255,255,255,255,255,255};
    int k[10] = {0};
    int gArrow_y = 0;


    int picking = 1;
    int checking = -1;

    int score_board = 0;


    int level1 = 0;



    int level_selection_boku = 1;
    int playing = 0;
    int bokuLevelLocked[9] = {1, 1, 1 ,1 ,1,1,1,1};
    int finished_score_board = 0;
    int mark = 0;
    int level = 1 ;
    float time = 0;
    int accuracy = 0 ;
    int score = 0;
    bool loadedScoreBoardText = false;




    int j = 1;//for the intro animation

    int clock = 0;
    int passed = 0;

    gBackground.setAlpha(a);
    gCurrentTexture = 0;

    SDL_Rect answerRect = { 200, 350, 300 , 125 };
    SDL_Rect answerLightRect = { 250, 372 , 240 , 23 };
    SDL_Rect answerRightRect  = { 250, 372 , 240 , 23 };

    SDL_Rect gLightRectSelectLevel = { 308,177 ,82 ,20} ;
    SDL_Rect gBlackRectSelectLevel = {150 ,100 , 420 ,380 };
    int selectedLevel = 1;

    int choix[10];


    int level_1_choix[10] = {2, 1,3,3,2,2,1,3,2,1};
    while (!quit)
    {
        while (SDL_PollEvent(&e) != 0)
        {
            if (e.type == SDL_QUIT)
            {
                 quit = true;
            }
            else if (e.type == SDL_KEYDOWN)
            {
                if (e.key.keysym.sym == SDLK_RETURN && playing)
                {
                    if (gCurrentTexture <10 )
                    {
                        if ( picking)
                        {
                            if (gArrow_y == 0)
                            {
                                choix[gCurrentTexture] = 1;
                            }
                            else if ( gArrow_y == 27)
                            {
                                choix[gCurrentTexture] = 2;
                            }
                            else
                            {
                                choix[gCurrentTexture] = 3;
                            }

                            picking = 0;
                            if (choix[gCurrentTexture] == level_1_choix[gCurrentTexture])
                            {
                                checking = 1;
                                mark += 1;
                            }
                            else
                            {

                                checking = 0;
                            }
                            answerRightRect.y += 27*(level_1_choix[gCurrentTexture] - 1);

                        }
                        else
                        {
                            if (gCurrentTexture <9 ) {gCurrentTexture += 1; }
                            else
                            {
                                if (gCurrentTexture == 9)
                                {
                                    score_board = 1;
                                }




                            }

                            gArrow_y = 0;
                            answerLightRect.y = 372;
                            answerRightRect.y = 372;
                            time += (float)clock / 1200.00;
                            clock = 0;
                            picking = 1;
                            passed = 0;
                            checking = -1;

                        }


                    }


                }
                else if ( picking)
                {
                    if (e.key.keysym.sym == SDLK_DOWN)
                    {
                        if (gArrow_y < 27*2)
                        {
                            answerLightRect.y += 27;
                            gArrow_y += 27;

                        }
                    }

                    else if (e.key.keysym.sym == SDLK_UP)
                    {
                        if (gArrow_y > 0)
                        {
                            answerLightRect.y -= 27;
                            gArrow_y -= 27;

                        }

                    }

                }

                /*if (score_board){

                    if  (e.key.keysym.sym == SDLK_RETURN)
                    {

                        score_board = 0;
                        level_selection_boku = 1;
                        playing = 0;

                    }


                }*/




                if (level_selection_boku)
                {
                    if (e.key.keysym.sym == SDLK_DOWN)
                    {
                        if ( gLightRectSelectLevel.y < 335)
                        {
                            gLightRectSelectLevel.y+= 21;
                            selectedLevel++;
                        }

                    }
                    else if (e.key.keysym.sym == SDLK_UP)
                    {
                        if ( gLightRectSelectLevel.y > 177)
                        {
                            gLightRectSelectLevel.y -= 21;
                            selectedLevel--;
                        }
                    }
                    else if ( e.key.keysym.sym == SDLK_RETURN)
                    {
                        if ( selectedLevel == 1 )
                        {
                            level_selection_boku = 0;
                            level = selectedLevel;
                            level1 = 1;

                        }
                    }
                }
                if ( score_board == 1 )
                {
                    if (e.key.keysym.sym == SDLK_SPACE )
                    {

                        score_board = 0;
                        playing = 0;
                        gCurrentTexture = 0;

                        level_selection_boku = 1;
                        if ( mark >= 7)
                        {
                            bokuLevelLocked[level-1] = 0;
                        }

                    }
                }
            }
        }
        //clear the screen
        SDL_SetRenderDrawColor(gRenderer,0,0,0,0);
        SDL_RenderClear(gRenderer);
        if ( level_selection_boku)
        {
            gBackground.render(0,0);
            gBackground.setAlpha(255);

            SDL_SetRenderDrawColor(gRenderer,0,0,0,0);
            SDL_RenderFillRect(gRenderer,&gBlackRectSelectLevel);

            SDL_SetRenderDrawColor(gRenderer,255,255,80,0);
            SDL_RenderFillRect(gRenderer,&gLightRectSelectLevel);

            glevelSelectionBoku.render(0,0);
            for (int i = 0 ; i < 8 ; i++)
            {
                if ( bokuLevelLocked[i] == 1){
                    glockIcon.render(290,200+i*21);}
            }


        }
        if (level1)
        {
            SDL_SetRenderDrawColor(gRenderer,255,255,255,0);
            SDL_RenderClear(gRenderer);
            if( Mix_PlayingMusic() == 0 )
            {
                Mix_PlayMusic( gMusicIntro, 1 );
            }


            for(int i = 0 ; i <= j/1650; i++)
            {
                gIntroFrames[i].render(0,0);
            }
            for (int i = 0 ; i <= j/1200-1 && i <10;i++)
            {

                gIntroFrames[i].setAlpha(gIntroFramesAlpha[i]);
                if (gIntroFramesAlpha[i]>0){
                    gIntroFramesAlpha[i] -= k[i]/4000;
                    k[i]++;
                }



            }

            j++;

            if (j/1650>= 10)
            {
                level1 = 0;
                playing = 1;
            }
        }
        else if (playing)
        {
            //Render the background
            gBackground.render(0,0);
            gBackground.setAlpha(a);
            if (score_board == 0)
                {
                //Render texture 1 to the screen
                gTextures[gCurrentTexture].renderOutlinedCentered();
                SDL_SetRenderDrawColor(gRenderer,0,0,0,0);
                SDL_RenderFillRect(gRenderer , &answerRect);

                if (picking == 0){
                    SDL_SetRenderDrawColor(gRenderer,0,255,0,0);
                    SDL_RenderFillRect(gRenderer, &answerRightRect);


                }


                if(picking)
                {
                    SDL_SetRenderDrawColor(gRenderer,255,255,80,0);
                }
                else if (checking)
                {
                    SDL_SetRenderDrawColor(gRenderer,0,255,0,0);
                }
                else
                {
                    SDL_SetRenderDrawColor(gRenderer,255,0,0,0);
                }


                SDL_RenderFillRect(gRenderer, &answerLightRect);

                gTexts[gCurrentTexture].render(255,370);
                gArrow.render(225,377+gArrow_y);
                gClockFrames[10-clock/1200].render( 650 ,30 );
                if (10-clock/1200 > 0 && picking) { clock++; }
                if ( 10-clock/1200 <= 0 && passed < 1)
                {
                    picking = 0;
                    choix[gCurrentTexture] = gArrow_y/27+1;

                    if (choix[gCurrentTexture] == level_1_choix[gCurrentTexture])
                    {
                        checking = 1;
                    }
                    else
                    {

                        checking = 0;
                    }
                    answerRightRect.y += 27*(level_1_choix[gCurrentTexture] - 1);
                    passed ++;
                }


                if ( checking == 1)
                {
                    gCorrectAnswerText.render(300,325);
                }
                else if ( checking == 0 )
                {
                    gWrongAnswerText.render(300,325);
                }
                if ( checking != -1 )
                {
                    gPressEnterText.render(260,475);
                }
            }

            else if ( score_board == 1)
            {
                if (!loadedScoreBoardText)
                {

                    SDL_Color textColor = { 255, 0, 0 };
                    char text[20];
                    itoa(mark,text,10);
                    strcat(text,"/10");
                    if( !gMarkText.loadFromRenderedText( text , textColor ) )
                    {
                        printf( "Failed to render text texture!\n" );
                    }
                    itoa(level,text,10);
                    if( !gLevelText.loadFromRenderedText( text , textColor ) )
                    {
                        printf( "Failed to render text texture!\n" );
                    }
                    itoa(time,text,10);
                    strcat(text,"s");

                    if( !gTimeText.loadFromRenderedText( text , textColor ) )
                    {
                        printf( "Failed to render text texture!\n" );
                    }
                    accuracy = (int)(((float)mark /10.00 )*100.00);
                    itoa(accuracy,text,10);
                    strcat(text,"%");

                    if( !gAccuracyText.loadFromRenderedText( text , textColor ) )
                    {
                        printf( "Failed to render text texture!\n" );

                    }

                    score =((100-time)+accuracy)*level;
                    itoa(score,text,10);
                    if( !gScoreText.loadFromRenderedText( text , textColor ) )
                    {
                        printf( "Failed to render text texture!\n" );

                    }


                    loadedScoreBoardText = true;
                }

                gMidoriyaFullBody.render(5,25);
                a = 45;
                SDL_Rect score_boardRect = { 350 , 130 , 300, 400 };
                SDL_SetRenderDrawColor(gRenderer,0,0,0,0);
                SDL_RenderFillRect(gRenderer,&score_boardRect);
                if ( mark >=9)
                {
                    gScoreBoard100.render(350,130);
                }
                else if (mark >= 7)
                {
                    gScoreBoard70.render(350,130);
                }
                else if ( mark >= 5)
                {
                    gScoreBoard50.render(350,130);
                }
                else
                {
                    gScoreBoard.render(350,130);
                }

                gMarkText.render(530,280);
                gLevelText.render(530,189);
                gTimeText.render(530,234);
                gAccuracyText.render(530,327);
                gScoreText.render(530,372);
                gPressEnterText.render(400,530);

            }
        }
        //update the screen
        SDL_RenderPresent(gRenderer);
    }



    close();
    return 0;
}
