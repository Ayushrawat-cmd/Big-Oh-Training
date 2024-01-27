/*
Name:- Ayush Rawat
Designation:- Technical Graduate Trainee
*/
#include <bits/stdc++.h>
using namespace std;

#define ll long long

mt19937 mt_rng(chrono::steady_clock::now().time_since_epoch().count()); // generate random values
ll randint(ll a, ll b) {
    return uniform_int_distribution<ll>(a, b)(mt_rng);
}


/*
Check whether we got the winner or not or is it draw
*/
int winner(vector<vector<char>>&board, char move){
    vector<int>row(3,0), col(3,0);
    int dash = 0;
    for(int i =0 ;i<3; i++){ // loop to find the number of desired character in the row and col
        for(int j=0; j<3; j++){
            if(board[i][j] == move){
                row[i]++;
                col[j]++;
            }
            else if(board[i][j] == '_')
                dash++;
        }
    }
    
    for(int idx =0; idx<3; idx++){
        if(row[idx] == 3) // found the winner on the basis of row
            return 1;
        if(col[idx] == 3) // found the winner on the basis of column
            return 1;
    }
    int idx = 0;
    int moves = 0;
    for(int i =0; i<3; i++){ // check for right diagonal
        if(board[i+idx][i+idx] == move)
            moves++;
    }
    if(moves == 3)
        return 1;
    moves= 0;
    int r = 0, c = 2;
    for(int i =0; i<3; i++){ // check for left diagonal
        if(board[r+i][c-i] == move)
            moves++;
    }
    if(moves == 3)
        return 1;
    if(dash == 0)
        return 2;
    return 0;
}
/*
Print the grid of the tic tac toe
*/
void printGrid(vector<vector<char>>board){
    for(vector<char> vec: board){
        for(char ch: vec){
            cout<<ch<<"\t";
        }
        cout<<'\n';
    }
}
/*
if computer not safe then we make it safe by playing the move in that position
*/
bool isComputerNotSafe(vector<vector<char>>&board, char move){
    char computer_move = move == 'O'?'X':'O';
    for(int i=0; i<3; i++){ // check for rows
        bool safe =0;
        int dash = 0, moves = 0;
        int r, c;
        for(int j=0; j<3; j++){
            if(board[i][j] == move)
                moves++;
            else if(board[i][j] == '_'){
                r = i, c= j;
                dash++;
            }
        }
        if(moves == 2 && dash == 1){
            board[r][c] =computer_move;
            return false;
        }
    }
    for(int j=0; j<3; j++){ // check for columns
        bool safe =0;
        int dash = 0, moves = 0;
        int r, c;
        for(int i=0; i<3; i++){
            if(board[i][j] == move)
                moves++;
            else if(board[i][j] == '_'){
                r = i, c= j;
                dash++;
            }
        }
        if(moves == 2 && dash == 1){
            board[r][c] = computer_move;
            return false;
        }
    }
    int r, c;
    int idx =0;
    int dash = 0, moves = 0;
    for(int i=0; i<3; i++){ // check for right diagonals
        if(board[idx+i][idx+i] == move)
            moves++;
        else if(board[idx+i][idx+i] == '_'){
            r = idx+i, c= idx+i;
            dash++;
        }
    }
    if(moves == 2 && dash == 1){
        board[r][c] = computer_move;
        return false;
    }
    int i =0, j=2;
    dash = 0, moves = 0;

    for(int idx=0; idx<3; idx++){ // check for left diagonals
        if(board[idx+i][j-idx] == move)
            moves++;
        else if(board[idx+i][j-idx] == '_'){
            r = idx+i, c= j-idx;
            dash++;
        }
    }
    if(moves == 2 && dash == 1){
        board[r][c] = computer_move;
        return false;
    }
    return true;
}

/*
function to check wehter the computer is winning of not . If its winning then we will make that move and wins the game.
*/
bool computerNotChanceOfWinning(vector<vector<char>>&board, char computer_move){
    for(int i=0; i<3; i++){ // check for rows
        bool safe =0;
        int dash = 0, moves = 0;
        int r, c;
        for(int j=0; j<3; j++){
            if(board[i][j] == computer_move)
                moves++;
            else if(board[i][j] == '_'){
                r = i, c= j;
                dash++;
            }
        }
        if(moves == 2 && dash == 1){
            board[r][c] =computer_move;
            return false;
        }
    }
    for(int j=0; j<3; j++){ // check for columns
        bool safe =0;
        int dash = 0, moves = 0;
        int r, c;
        for(int i=0; i<3; i++){
            if(board[i][j] == computer_move)
                moves++;
            else if(board[i][j] == '_'){
                r = i, c= j;
                dash++;
            }
        }
        if(moves == 2 && dash == 1){
            board[r][c] = computer_move;
            return false;
        }
    }
    int r, c;
    int idx =0;
    int dash = 0, moves = 0;
    for(int i=0; i<3; i++){ // check for right diagonals
        if(board[idx+i][idx+i] == computer_move)
            moves++;
        else if(board[idx+i][idx+i] == '_'){
            r = idx+i, c= idx+i;
            dash++;
        }
    }
    if(moves == 2 && dash == 1){
        board[r][c] = computer_move;
        return false;
    }
    int i =0, j=2;
    dash = 0, moves = 0;

    for(int idx=0; idx<3; idx++){ // check for left diagonals
        if(board[idx+i][j-idx] == computer_move)
            moves++;
        else if(board[idx+i][j-idx] == '_'){
            r = idx+i, c= j-idx;
            dash++;
        }
    }
    if(moves == 2 && dash == 1){
        board[r][c] = computer_move;
        return false;
    }
    return true;
}


/*
choice made by the computer
*/
void computerChoice(vector<vector<char>>&board, bool first_turn, char user_character){
    int computer_row, computer_col;
    char computer_char = user_character == 'O'?'X':'O';
    if(first_turn){ // if the computer having the first turn
        do{
            computer_row = randint(0,2);
            computer_col = randint(0,2);
        }while(board[computer_row][computer_col]== user_character);
        board[computer_row][computer_col] = computer_char;
    }
    else{
        if(computerNotChanceOfWinning(board, computer_char)){ // if not wins then run the following code
            if(isComputerNotSafe(board, user_character)){ // if computer is not safe then run the following code
                do{
                    computer_row = randint(0,2);
                    computer_col = randint(0,2);
                }while(board[computer_row][computer_col]== user_character); // random values made by the board
                    board[computer_row][computer_col] = computer_char;
                }

            }
    }
}


/*
 function to check wether move made by the user is right or not
*/
bool validMove(vector<vector<char>>&board, int row, int col){ 
    return ( row>=0 && col>=0 && row<3 && col<3 && board[row][col] == '_');
}


/*
function get calls if the user having the first turn
*/
void firstUserTurn(vector<vector<char>>&board, char user_character, char computer_character, bool first_time){
    cout<<"Now enter your turn:- ";
    int user_row, user_col;
    cin>>user_row>>user_col;
    while(!(validMove(board, user_row, user_col))){
        cout<<"Please enter the valid move which contains '_' and within the matrix such that row >=0 and column>=0 and row<3 and column <3:- ";
        cin>>user_row>>user_col;
    }
    board[user_row][user_col] = user_character;
    printGrid(board);
    if(winner(board, user_character) == 1){ 
        cout<<"Congratulations, You are the winner!\n";
        return ;
    }
    else if(winner(board, user_character) == 2){
        cout<<"It's a draw!\n";
        return ;
    }
    cout<<"Now computer's turn\n";
    computerChoice(board, first_time, user_character);
    printGrid(board);
    if(winner(board, computer_character) == 1){
        cout<<"Yay!, I won\n";
        return ;
    }
    if(winner(board, computer_character) == 2){
        cout<<"It's a draw!\n";
        return ;
    }
    firstUserTurn(board, user_character, computer_character,0);
}


/*
function get call if the computer's having the first turn
*/
void firstComputerTurn(vector<vector<char>>&board, char user_character, char computer_character, bool first_time){
    cout<<"Now computer's turn\n";
    computerChoice(board, first_time, user_character);
    printGrid(board);
    if(winner(board, computer_character) == 1){
        cout<<"Yay!, I won\n";
        return ;
    }
    if(winner(board, computer_character) == 2){
        cout<<"It's a draw!\n";
        return ;
    }
    cout<<"Now enter your turn:- ";
    int user_row, user_col;
    cin>>user_row>>user_col;
    while(!(validMove(board, user_row, user_col))){
        cout<<"Please enter the valid move which contains '_' and within the matrix such that row >=0 and column>=0 and row<3 and column <3:- ";
        cin>>user_row>>user_col;
    }
    board[user_row][user_col] = user_character;
    printGrid(board);
    if(winner(board, user_character) == 1){
        cout<<"Congratulations, You are the winner!\n";
        return ;
    }
    else if(winner(board, user_character) == 2){
        cout<<"It's a draw!\n";
        return ;
    }
    firstComputerTurn(board, user_character, computer_character,0);
}
int main(){
    cout<<"TIC TAC TOE\n";
    cout<<"_\t_\t_\n_\t_\t_\n_\t_\t_\n";
    vector<vector<char>>board(3,vector<char>(3, '_'));
    char choice ;
    do{
        string turn_choice;
        cout<<"Do you want first turn (Type 'Y'  or 'N'):- ";

        cin>>turn_choice;
        if(turn_choice == "Y"){
            cout<<"Enter the row number and column number where you want to place the sign\nFor example:- '0 0','0 1' etc. \n";
            char user_character;
            cout<<"Choose character 'O' or 'X'\n";
            cin>>user_character;
            while(user_character!='O' && user_character != 'X'){
                cout<<"Please choose correct character 'O' or 'X':- ";
                cin>>user_character;
            }
            char computer_character = user_character == 'O'?'X':'O';
            firstUserTurn(board, user_character, computer_character,1);
        }
        else if(turn_choice == "N"){
            cout<<"Enter the row number and column number where you want to place the sign as here is the 0 based indexing.\nFor example:- '0 0','0 1' etc. \n";
            firstComputerTurn(board, 'O', 'X', 1);
        }
        else{
            cout<<"Wrong choice.\n";
        }
        cout<<"Do you want to play again? (Type 'Y' or 'N'):- ";
        for(int i =0; i<3; i++){
            for(int j =0; j<3; j++)
                board[i][j] = '_';
        }
        cin>>choice;
        while(choice!='Y' && choice!='N' ){
            cout<<"Please enter the valid choice ('Y' or 'N'):- ";
            cin>>choice;
        }
    }while(choice == 'Y');
        
}