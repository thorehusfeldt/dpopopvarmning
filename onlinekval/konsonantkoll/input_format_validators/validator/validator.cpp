#include "validator.h"

bool isConsonant(char c) {
    const string consonants = "bcdfghjklmnpqrstvwxz";
    return consonants.find(c) != string::npos;
}

void run() {
    bool allowSpaces = Arg("allowSpaces");
    int maxRepeated = Arg("maxRepeated");
    int maxLength = Arg("maxLength");

    string in = Line();
    Eof();

    // String length
    assert(in.size() <= maxLength);

    // Spaces
    bool hasSpace = in.find(' ') != string::npos;
    assert(!(hasSpace && !allowSpaces));

    // Only a-z and space
    for (char c : in) assert((c >= 'a' && c <= 'z') || c == ' ');

    // Max repeated
    int maxCount = 0;
    char prev = -1;
    int count = 0;
    for (char c : in) {
        if (c == prev)
            count++;
        else {
            prev = -1;
            maxCount = max(count, maxCount);
            if (isConsonant(c)) {
                prev = c;
                count = 1;
            } else {
                prev = -1;
                count = 0;
            }
        }
    }
    maxCount = max(count, maxCount);
    assert(maxCount <= maxRepeated);
}

