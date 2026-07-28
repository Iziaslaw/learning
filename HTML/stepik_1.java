/*Exemple 1*/
public class Main {
    public static void main(String[] args) {
        System.out.println("It's alive! It's alive!");
    }
}

/*Exemple 2*/

import java.security.MessageDigest;

public class Quiz {

    public static void main(String[] args) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest("abracadabra".getBytes("UTF-8"));
        for (byte b : digest) {
            System.out.printf("%02x", b);
        }
    }
}

/*Exemple 3*/

public static boolean booleanExpression(boolean a, boolean b, boolean c, boolean d) {
    return a & b & !c & !d || a & !b & !c & d || !a & b & !c & d || !a & b & c & !d || a & !b & c & !d || !a & !b & c & d ;
}

/*ex4 количество високосных годов от РХ*/

public static int leapYearCount(int year) {
    return year / 4 - year / 100 + year / 400;
}

/*ex5 */
char literal = 'a'
char tab = '\t'
char lineFeed = '\n'
char carriageReturn = '\r'
char singleQuote = '\''
char backslash = '\\'
char hex = '\u03A9'
String name = "Ilia"

double simple = -1.234;
double exponential = -123.4e-2;
double hex = 0x1.Fp10;
float floatWithSuffix = 36.6f;
double doubleWithSuffix = 4d;

/*ex 6*/
public static boolean doubleExpression(double a, double b, double c) {
    return Math.abs(a + b - c) < 0.0001;
}

/*ex 7*/
byte a = -128 /* по ум. 0, 8-разрядным знаковым целым числом, -2^7 2^7-1 byte */
short r = -32,768 /* по ум. 0, 16-разрядным знаковым целым числом, -2^15 2^15-1 short */
int a = -2,147,483,648 /* по ум. 0, 32-разрядным знаковым целым числом, -2^31 2^31-1 int */
long a = -9,223,372,036,854,775,808L /* по ум. 0L, 64-разрядным знаковым целым числом -2^63 2^63-1 long */
float f1 = 234.5f /* по ум. 0.0f, c одинарной точностью 32-битный IEEE 754 с плавающей точкойfloat */
double d1 = 123.4; /* по ум. 0.0d, 64-битный IEEE 754 с плавающей точкой double */
boolean one = true; /* по ум. false, один бит, boolean */
char letterA = 'A'; /* char от \u0000 до \uffff*/
Animal animal = new Animal("giraffe");/* */
//ex 8 меняет в числе переведенном в битовое поле бит под определенным индексом
public static int flipBit(int value, int bitIndex) {
    return value ^ 1 << bitIndex - 1;
}

//2.2 Преобразование типов
byte byteValue = 123;
short shortValue = byteValue;
int intValue = shortValue;
long longValue = intValue;

char charValue = '@';
int intFromChar = charValue;
long longFromChar = charValue;

float floatFromLong = longValue;
double doubleFromFloat = floatFromLong;
double doubleFromInt = intValue;

//
int intValue = 1024;
byte byteValue = (byte) intValue;// 0

double pi = 3.14;
int intFromDouble = (int) pi; // 3

float largeFloat = 1e20f;                 // 10^20
int intFromLargeFloat = (int) largeFloat; // 2*10^9

double largeDouble = 1e100;
float floatFromLargeDouble = (float) largeDouble; // oxo

//
byte b = -1;
b >>>= 7;// b = (byte) (b >>> 7);

//возвращает букву, стоящую в таблице UNICODE после символа "\" (обратный слэш) на расстоянии a.
public static char charExpression(int a) {
    int charValue = '\\';
    int charValueFromInt = charValue + a;
    //int charValue2 = charValueFromInt + a;
    return (char) charValueFromInt;
}


/*ex 01*/
import java.util.Scanner;

class MyNumber {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int x = sc.nextInt(), y = sc.nextInt();       
       int myVar = x + y;
       System.out.print(myVar);
   }
}
// print name
class GetName {
    public static void main(String[] args) {
        String name = "Ivan";
        System.out.println(name);
    }
}
/*Scanner*/

import java.util.Scanner;

class MyClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(sc.nextLine());
    }
}

import java.util.Scanner;

class MyClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        double y = sc.nextDouble();
        String s = sc.nextLine();
    }
}

import java.util.Scanner;
class MySolution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Привет, " + sc.nextLine());
    }
}

import java.util.Scanner;
class MySolution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.print(s);  
        System.out.println(" " + s);
        System.out.println(s);
        System.out.println(s);
    }
}

//
import java.util.Scanner;
class MySolution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.next();
        String s2 = sc.next();
        String s3 = sc.next();
        System.out.println(s3 + ":" + s2 + ":" + s1);
    }
}

//
import java.util.Scanner;
class MySolution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        String s3 = sc.nextLine();
        System.out.println("Привет, " + s1 + ", это твой помощник " + s2 + ".\nУ тебя " + s3 + " новых писем.");
    }
}

//test input: 8 11
import java.util.Scanner;
class MyNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int myVar = sc.nextInt() + sc.nextInt();
        System.out.println(myVar);
   }
}

//
import java.util.Scanner;
class MyNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x = sc.nextDouble(), y = sc.nextDouble();
        System.out.println((double) x *y);
        System.out.println((double) (x+y)*2);
   }
}

import java.util.Scanner;
class MyNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        System.out.print(x + " ");
        System.out.print(x*x + " ");
        System.out.print(x*x*x);
    }
}

//
import java.util.Scanner;
class MyNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int d = x % (24*60*60);
        int h = d / 3600;
        int m = d % 3600 / 60;
        int s = d % 3600 % 60;
        System.out.println(h/10+""+h%10+":"+m/10+""+m%10+":"+s/10+""+s%10);
        //System.out.format("%02d"+":"+"%02d"+":"+"%02d", h, m, s);
   }
}

//Инкремент префикс ++x, декремент префикс --x 

int x = 50;
int y = ++x; // x == 51, y == 51

//Инкремент постфикс

int x = 50;
int y = x++; // x == 51, y == 50

//
class MyNumber {
    public static void main(String[] args) {
        int x = 10;
        System.out.print(++x +"\n"+ ++x +"\n"+ ++x);
    }
}

//Методы строк 
//Длина строки str.length()
str.length(); // возвращает длину строки str (количество символов, включая пробелы)

String word = "Java is strong";
int x = word.length();
System.out.println(x); // 14
//сравнение строк str1.equals(str2); boolean
String word1 = "Java";
String word2 = "Python";
System.out.println(word1.equals(word2)); // false

String word3 = "Ja";
String word4 = "va";
boolean result = word1.equals(word3 + word4); 
System.out.println(result); // true
//Получение индекса элемента в строке .indexOf()
String word = "abracadabra";
int x = word.indexOf('b');
System.out.println(x); // 1

int y = word.indexOf('Z');
System.out.println(y); // -1
//Получение элемента строки по его индексу charAt() возвращает char
String word = "abracadabra";

char letter_0 = word.charAt(0);
System.out.println(letter_0); // a

char letter_4 = word.charAt(4);
System.out.println(letter_4); // c
//7 Проверка строки на пустоту isEmpty()
String str1 = "Hubba Bubba";
String str2 = "   ";
String str3 = "";

boolean value1 = str1.isEmpty(); // false
boolean value2 = str2.isEmpty(); // false
boolean value3 = str3.isEmpty(); // true
//Одна строка внутри другой contains()
String str1 = "One Two Three";
String str2 = "One";
String str3 = "Four";

boolean value1 = str1.contains(str2); // true
boolean value1 = str1.contains(str3); // false
//8 Преобразование регистров toUpperCase() / toLowerCase()
String s = "I'll be back";

System.out.println(s.toLowerCase()); // i'll be back
System.out.println(s.toUpperCase()); // I'LL BE BACK
//Представление числа в строковом формате toString() Integer
int n = 12345;                      // Это число типа int
System.out.println(n);              // 12345 

String str1 = Integer.toString(n);  // Это строка
System.out.println(str1);           // 12345

Integer num = n;                    // Это число-объект класса Integer
System.out.println(num);            // 12345

String str2 = num.toString();        // Это строка
System.out.println(str2);            // 12345
//9 Преобразование строки в число valueOf() Integer
String str = "12345";

int num = Integer.parseInt(str);    //num - переменная типа int
System.out.println(num);            //12345
//преобразование строки в число с плавающей точкой Double
String str = "12345";

double num = Double.parseDouble(str);    //num - переменная типа double
System.out.println(num);                 //12345.0
//10 Создание подстроки substring()
String str = "Добро пожаловать в мир Java!";

System.out.println(str.substring(6));         //пожаловать в мир Java!

System.out.println(str.substring(6, 15));     //пожаловат
//Замена  элементов строки replace() элементы типа char
String str = "Добро пожаловать в мир Java!";

System.out.println(str.replace('о', 'А')); //ДАбрА пАжалАвать в мир Java!

//
import java.util.Scanner;
class MyProgram {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       String text = sc.nextLine();
       int num = sc.nextInt();
       char letter = text.charAt(num-1);
       System.out.print(letter);
       
   }
}

import java.util.Scanner;
class MyProgram {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       String str1 = sc.nextLine();
       String str2 = sc.nextLine();
       boolean result = str1.equals(str2);
       System.out.print(result);
       
   }
}

import java.util.Scanner;
class MyProgram {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);
        int a = myScanner.nextInt(), b = myScanner.nextInt();
        System.out.println(a + b + "\n" + Integer.toString(a)+ Integer.toString(b));
    }
 }
 
 //
 int x = 10, y = 15;

System.out.println(x + 1 + " не равно " + y);   //11 не равно 15
System.out.println(x + " не равно " + y + 1);   //10 не равно 151
System.out.println(x + " не равно " + (y + 1)); //10 не равно 16

//
import java.util.Scanner;
class MyProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next(), b = sc.next();
        System.out.println(a.charAt(0) < b.charAt(0));
    }
}

//Сумма и произведение корней уравнения по теореме Виета
import java.util.Scanner;
class MyProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double a = sc.nextDouble(), b = sc.nextDouble(), c = sc.nextDouble();
        System.out.print((-b/a)+" "+(c/a));
    }
}

//Сравнение длины строк 
import java.util.Scanner;
class MyProg {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        String x = sc.nextLine(), y = sc.nextLine();
        if (x.length() > y.length()) {
            System.out.print("Махатма");
        } else {
            System.out.print("Джавахарлал");
        }
	}
}

//Тернарный оператор
int x = 15;

System.out.println((x % 2 == 0) ? "Число чётное" : "Число нечётное");

//
import java.util.Scanner;
class MyProg {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        System.out.print((x==3 || x==4 || x==5) ? "YES" : "NO");
	}
}

import java.util.Scanner;
class MyProgram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int x = sc.nextInt(), y = sc.nextInt();
        System.out.print((x+y)%2==0 && (x*y)%2!=0);
	}
}

import java.util.Scanner;
class MyProgram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int x = sc.nextInt(), y = sc.nextInt(), z = sc.nextInt();
        System.out.print(x%2+y%2+z%2==1);
	}
}
// Рассчет валидности даты
import java.util.Scanner;
class MyProgram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int d = sc.nextInt(), m = sc.nextInt(), y = sc.nextInt();
        boolean vis = y%4==0&&y%100!=0||y%4==0&&y%400==0;
        boolean val;
		if(1<=d<=31 && 1<=m<=12 && y>=1) {
            if(vis){
                if((m==1||m== 3||m== 5||m== 7||m== 8||m== 10||m== 12)&&d<=31){
                    val = true;}
                if(m==2&&d<=29){
                    val = true;}
                if((m==4||m==6||m==9||m==11)&&d<=30){
                    val =true;
				}
			}else{
                if((m==1||m== 3||m== 5||m== 7||m== 8||m== 10||m== 12)&&d<=31){
                    val = true;}
                if(m==2&&d<=28){
                    val = true;}
                if((m==4||m==6||m==9||m==11)&&d<=30){
                    val =true;
                }
            }
		}
        System.out.print(val);
	}
}
//чужое
import java.util.Scanner;
class MyProgram {
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int d = sc.nextInt();
	int m = sc.nextInt();
	int y = sc.nextInt();
	boolean a = (m==1||m==3||m==5||m==7||m==8||m==10||m==12)&&(d<32)&&(d>0)&&(y>=0);
	boolean b = (m==4||m==6||m==9||m==11)&&(d<31)&&(d>0)&&(y>=0);
	boolean c = (m==2)&&(d<29)&&(d>0)&&(y>=0);
	boolean z = (m==2)&&(d<30)&&(d>0)&&(((y%400==0)||(y%4==0))&&(y%100!=0));
	System.out.print(a||b||c||z);
	}
} 

//
import java.util.Scanner;
class MyProgram {
    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        String a= sc.next(),
        b=sc.next(),
        c=sc.next(), x;
        if (a.charAt(0)>b.charAt(0)){x=a;a=b;b=x;}
        if (b.charAt(0)>c.charAt(0)){x=b;b=c;c=x;}
        if (a.charAt(0)>b.charAt(0)){x=a;a=b;b=x;}
        
        
        
        System.out.print(a+"\n"+b+"\n"+c);

    }
}

//вывод среднего числа из трех
import java.util.Scanner;
class Example {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt(), y = sc.nextInt(), z = sc.nextInt();
        if((x>=y&&x<=z)||(x<=y&&x>=z)){System.out.print(x);}
        else if((y>=x&&y<=z)||(y<=x&&y>=z)){System.out.print(y);}
        else if((z>=x&&z<=y)||(z<=x&&z>=y)){System.out.print(z);}
    }
}

//разница между минимальным и максимальным числом
import java.util.Scanner;
class Example {
	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt(); int b = scan.nextInt();int c = scan.nextInt();int d=scan.nextInt(); 
        if ((a-b>d) || (a-c>d)  || (b-a>d) || (b-c>d) || (c-a>d) ||(c-b>d)){
           System.out.println("Ура, бастуем!");
           } else {
            System.out.println("За работу, Солнце ещё высоко");

    }
}
}

//Пересечение отрезков на числовой прямой
import java.util.Scanner;
class Example {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a1 = input.nextInt(), b1 = input.nextInt(), 
		a2 = input.nextInt(), b2 = input.nextInt();
        input.close();
        if (a2 > a1) a1 = a2;
        if (b2 < b1) b1 = b2;
        if (a1 < b1) System.out.print(a1+" "+b1);
        else if (a1 == b1) System.out.print(a1);
        else System.out.print("Пересечения нет");
}}

import java.util.Scanner;
class Exemple {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a1 = sc.nextInt(), b1 = sc.nextInt(), a2 = sc.nextInt(), b2 = sc.nextInt();
        if((a2-b1)*(b2-a1)<=0){
            if((a2-b1)*(b2-a1)<0){
                if(b2>b1&&b1-a2>0&&a2>=a1){System.out.print(a2+" "+b1);}
                if(b2<b1&&b2-a1>0&&b2>=b1){System.out.print(a1+" "+b2);}
                if(b2==b1&&a2>a1){System.out.print(a2+" "+b1);}
                if(b2==b1&&a2<a1){System.out.print(a1+" "+b2);}
                if(a2<a1&&b2>b1){System.out.print(a1+" "+b1);}
                if(a2>a1&&b2<b1){System.out.print(a2+" "+b2);}
                if(a1==a2&&b1==b2){System.out.print(a1+" "+b1);}
            }else{
                if(b2>b1&&b1-a2==0){System.out.print(a2);}
                if(b2<b1&&b2-a1==0){System.out.print(a1);}
            }
        }else{
            System.out.print("Пересечения нет");
        }
    }
}
//Наибольшее четное число из трёх
import java.util.Scanner;
class Example {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        if(a%2==0&&b%2==0&&c%2==0){
            System.out.print(Math.max(Math.max(a,b),c));
        }
        else if(a%2==0&&b%2==0&&c%2!=0){
            System.out.print(Math.max(a,b));
        }
        else if(a%2==0&&b%2!=0&&c%2==0){
            System.out.print(Math.max(a,c));
        }
        else if(a%2!=0&&b%2==0&&c%2==0){
            System.out.print(Math.max(b,c));
        }
        else if(a%2==0){
            System.out.print(a);
        }
        else if(b%2==0){
            System.out.print(b);
        }
        else if(c%2==0){
            System.out.print(c);
        }
        else if(a%2!=0&&b%2!=0&&c%2!=0){System.out.print("Чётных чисел нет");}
    }
}

                           _   _
            :               `v'
   `.       ;       .'                 ,~-.
     `.  .=:::=.  .',~')       _ _    (    )~.
       ;:::::::::; (    `-.   ' V `  ,'       )~.  _ _
      /:::::::::::;-`      )        (          __)' v `
     |:::::::::::(_         )~./\    `~'--~'`~' _
'''''|::::::::::::(_    __    /##\            ,' )_
      \:::::::::::/(   _HH_,~/#/\#\          ( c'  `._
       `:::::::::'  `~[____]/#/==\#\       ,-' -' (_c )
      .' `=:::=' `.    |=_|/#/= _=\#\      `>o  ~    '-.
    .'      ;      `.  |-=/#/=____=\#\     ( ~ ,~.~.,`-'),
     _  _   :        ` |=/#/=/,~~.\=\#\    ,' (\\||,' `O'),
   .' \/ `. :          |/#/=(/_)(_\)=\#\  (`~o(_\`|)o ~   )
                       /#/_= |_\/_|  _\#\  >(   `~' ._,~ '-.
                      /#/ _=[______]= _\#\(' `~,  c    ~. c)
                     /#/=,---. _ = ___ =\#\`( (  ~ _.'   <'
                    /#/ /_____\ ==/,-.\ =\#\(  c   c___ ) )
                    `|=(/_|_|_\) //.-.\\=_|' `-.__,' //`-'
                  `v@|==|_|_|_|=(/8|_|8\)=|   `,-\ `'/`,-
                `v@'~|= |_;_;_| =|88888| =|       \ |
        _/\_/\_,(c`@'|=[_______]=|888()|==|_/\_/\_| |/\_
        -||-||-@~'(_@|= _o@&8o_ =|88888| =|-||-||-( |||-
       _,@`v-@'~ c@._|_['%8o&8']_|88888|__| || || | )||
     ,@C @,~' @,-v~' ::`"""""""`[_______]::  :::  | | :
    'v-~,@,`    :  (\-/)   ::  : ;;;;;' `*~   _.-'   `-.
                  ={   }=   ~*' ;;;;;; ::   :   `*  ::::
     :::   `*  ::   ) (    ::    ;;;;;;.~*'  :::     hjw
            :     _/   \_     `*~ ;;;;;;;.::     ::    ::
         :: `*  ::\     / :::      ;;;;;;;;.`*'     ::
      *'           `-))'      `*'  ;;;;;;;;;.  :::  *'  ::
      :      :::    ((  :: `*        ;;;;;;;;;.
                     \)         ::
.
╱◥◣^^^^^^^^^
│∩│_◥███◣___╱◥███◣
╱◥◣___◥████◣▓∩▓│∩║
│╱◥█◣ ║∩∩∩║___◥█▓▓█◣
││∩│▓__║∩?│║▓ ▓ ▓∩ ▓║
.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•¬¬.¸
Perfect World
start elementclient.exe startbypatcher nocheck user:ЛОГИН pwd:ПАРОЛЬ role:НИКНЕЙМ

//возвращает букву, стоящую в таблице UNICODE после символа "\" (обратный слэш) на расстоянии a.
public static char charExpression(int a) {
    char charValue = '\\';
    int charValueFromInt = charValue + a;
    return (char) charValueFromInt;
}
//
boolean Boolean
byte Byte
short Short
int Integer
long Long
char Character
float Float
double Double
//Классы-Обертки
int primitive = 0;
Integer reference = Integer.valueOf(primitive);
int backToPrimitive = reference.intValue();
//
long fromString = Long.parseLong("12345");
String fromLong = Long.toString(12345);
String concatenation = "area" + 51;
//
short maxShortValue = Short.MAX_VALUE;
int bitCount = Integer.bitCount(123);
boolean isLetter = Character.isLetter('a');
float floatInfinity = Float.POSITIVE_INFINITY;
double doubleNaN = Double.NaN;
boolean isNaN = Double.isNaN(doubleNaN);
