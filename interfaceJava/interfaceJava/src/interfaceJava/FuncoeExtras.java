package interfaceJava;

import java.awt.Button;

import javax.swing.ImageIcon;
import javax.swing.JFileChooser;

public class FuncoeExtras {
	
	String arq;
	ImageIcon histo;
	ImageIcon imagem;
	String[] cmdExec;
	JFileChooser jfc;
	public String camImagem;
	Button btnDrt;
	
	public void definirDiretorios(int i) {
		
		if( i == 0 ) {//pessoal
			//Funcao substituirTexto
			arq = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\main.py",
	      		      "--img",
	      		      ""
    		    };
			cmdExec = entrada;
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens");	//pc pessoal
			
		}else { //projeto
			//Funcao substituirTexto
			arq = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
      		      "python",
      		      "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py",
      		      "--img",
      		      ""
      		    };
			cmdExec = entrada;
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\imagens");	//pc Projeto
		}

	}
	
	public void ExecutarScriptPython(String saida) {
        try {
        	cmdExec[3] = saida; 
		    Runtime.getRuntime().exec(cmdExec);
		    
		    Thread.sleep(2200);
		    
		    SubstituirTexto(saida);
		    SubstituirImagem(saida);


        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
}
