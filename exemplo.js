/*
 * ==========================================
 * Arquivo de Exemplo para o Smart Minifier
 * ==========================================
 * Este script contém intencionalmente:
 * - Múltiplas quebras de linha
 * - Espaços redundantes
 * - Comentários que devem ser ignorados
 */

class JogoEducativo {
    
    constructor( titulo, tema ) {
        this.titulo = titulo;
        this.tema = tema;
        this.pontuacao = 0;
    }

    // Método principal de inicialização
    iniciar() {
        
        console.log( `Iniciando a partida de: ${this.titulo}` );
        
        // Loop de simulação de pontos
        for ( let i = 0; i < 5; i++ ) {
            
            this.pontuacao += 10;
            
        }
        
        return this.pontuacao;
    }
}

const jogo = new JogoEducativo( "Palavras ao Ar", "Alfabetização e Descoberta" );
jogo.iniciar();


class ProdutoSustentavel {
    
    constructor( nome, ingredientes ) {
        
        this.nome = nome;
        this.ingredientes = ingredientes;
        
    }

    fabricar() {
        /* 
           Processo de fabricação sustentável
           Garante a mistura homogênea dos ingredientes
        */
        const base = this.ingredientes.join( " + " );
        
        return `Lote finalizado: ${this.nome}. Composição: ${base}`;
    }
}

const sabao = new ProdutoSustentavel( 
    "Meu Sabão Líquido", 
    [ "Óleo de cozinha reciclado", "Semente de algodão", "Base alcalina" ] 
);

console.log( sabao.fabricar() );