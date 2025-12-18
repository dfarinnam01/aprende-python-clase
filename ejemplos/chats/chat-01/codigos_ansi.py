class CodigosAnsi:
    RESET = "\033[0m"

    # ===== Estilos =====
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    FAST_BLINK = "\033[6m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    STRIKE = "\033[9m"

    # ===== Colores básicos =====
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # ===== Fondos básicos =====
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    BG_BRIGHT_GREEN= "\033[102m"
    # ================================
    #       Métodos utilitarios
    # ================================

    @staticmethod
    def apply(text, *codes):
        """Aplica múltiples códigos ANSI al texto."""
        return "".join(codes) + text + ANSI.RESET

    # ===== Colores avanzados ANSI 256 =====
    @staticmethod
    def color256(n):
        """Color de texto usando paleta ANSI 256."""
        return f"\033[38;5;{n}m"

    @staticmethod
    def bg256(n):
        """Color de fondo usando paleta ANSI 256."""
        return f"\033[48;5;{n}m"

    # ===== Colores RGB =====
    @staticmethod
    def rgb(r, g, b):
        """Color RGB de texto."""
        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def bg_rgb(r, g, b):
        """Color RGB de fondo."""
        return f"\033[48;2;{r};{g};{b}m"

    # ===== Control de cursor =====
    @staticmethod
    def move_up(n=1):
        return f"\033[{n}A"

    @staticmethod
    def move_down(n=1):
        return f"\033[{n}B"

    @staticmethod
    def move_right(n=1):
        return f"\033[{n}C"

    @staticmethod
    def move_left(n=1):
        return f"\033[{n}D"

    @staticmethod
    def goto(x, y):
        """Posiciona el cursor en la columna x, fila y."""
        return f"\033[{y};{x}H"

    # ===== Pantalla & líneas =====
    CLEAR = "\033[2J"            # Limpia pantalla
    CLEAR_LINE = "\033[2K"       # Limpia línea actual
    HOME = "\033[H"              # Va al inicio

    # ===== Ocultar / Mostrar cursor =====
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

    # ===== Scroll =====
    @staticmethod
    def scroll_up(n=1):
        return f"\033[{n}S"

    @staticmethod
    def scroll_down(n=1):
        return f"\033[{n}T"

    @staticmethod
    def activa(codigo:str):
        print(f"{codigo}",end="")

    @staticmethod
    def desactiva():
        print("\033[0m",end="")

    def texto_color(texto:str,color:str)->str:
        return f"{color}{texto}{CodigosAnsi.RESET}"

    def print_texto_color(texto:str,color:str,end="")->str:
        print(f"{color}{texto}{CodigosAnsi.RESET}",end=end)