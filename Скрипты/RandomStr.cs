using System;

class RandomString
{
    string letters = "QWERTYUIOPASDFGHJKLZXCVBNM";
    Random rand = new();

    public char NextString()
    {
        return letters[rand.Next(0, letters.Length)];
    }
}