import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;

public class H {
    InputStream is;
    PrintWriter out;
    String INPUT = "";
    
    void solve()
    {
        int n = ni();
        int Q = ni();
        par = new int[n];
        for(int i = 1;i < n;i++){
            par[i] = ni()-1;
        }
        par[0] = -1;
        int[][] g = parentToG(par);
        int[][] pars = parents3(g, 0);
        int[] ord = pars[1], dep = pars[2];
        clus = decomposeToHeavyLight(g,par, ord);
        cluspath = clusPaths(clus, ord);
        clusiind = clusIInd(cluspath, n);
        int m = cluspath.length;
        sts = new SegmentTreeMatrix[m];
        for(int i = 0;i < m;i++){
            sts[i] = new SegmentTreeMatrix(cluspath[i].length);
        }
        int[][] spar = logstepParents(par);
        
        for(int z = 0;z < Q;z++){
            char type = nc();
            if(type == 'U'){
                int x = ni()-1;
                long K = nl();
                sts[clus[x]].update(clusiind[x], K);
            }else{
                int mod = 1000000007;
                int x = ni()-1, y = ni()-1;
                int lca = lca2(x, y, spar, dep);
                long ret = d(x)+d(y)-d(lca)-d(par[lca]);
                ret %= mod;
                if(ret < 0)ret += mod;
                out.println(ret);
            }
        }
    }
    
    int[] par;
    int[] clus, clusiind;
    int[][] cluspath;
    SegmentTreeMatrix[] sts;
    
    long d(int x)
    {
        if(x == -1)return 0;
        int[] lcx = new int[100];
        int[] lto = new int[100];
        int p = 0;
        int cx = clus[x];
        int ind = clusiind[x];
        while (true) {
            lcx[p] = cx;
            lto[p] = ind+1;
            p++;
            int con = par[cluspath[cx][0]];
            if(con == -1)break;
            ind = clusiind[con];
            cx = clus[con];
        }
        int[] v = {0, 0, 1, 0};

        for(int i = p-1;i >= 0;i--){
            v = sts[lcx[i]].apply(0, lto[i], v);
        }
        return v[3];
    }
    
    public static class SegmentTreeMatrix {
        public int M, H, N;
        public int[][][] node;
        public static int mod = 1000000007;
        public static long BIG = 8L*mod*mod;
        public static int S = 4;
        
        public SegmentTreeMatrix(int n)
        {
            N = n;
            M = Integer.highestOneBit(Math.max(N-1, 1))<<2;
            H = M>>>1;
            
            node = new int[M][][];
            for(int i = 0;i < N;i++){
                node[H+i] = new int[S][S];
                node[H+i][0][0] = 1;
                node[H+i][0][1] = 1;
                node[H+i][1][0] = 1;
                node[H+i][3][1] = 1;
                node[H+i][2][2] = 1;
                node[H+i][3][3] = 1;
                node[H+i][3][0] = 1;
            }
            
            for(int i = H-1;i >= 1;i--)propagate(i);
        }
        
        private void propagate(int cur)
        {
            node[cur] = prop2(node[2*cur], node[2*cur+1], node[cur]);
        }
        
        private int[][] prop2(int[][] L, int[][] R, int[][] C)
        {
            if(L != null && R != null){
                C = mul(R, L, C, mod);
                return C;
            }else if(L != null){
                return prop1(L, C);
            }else if(R != null){
                return prop1(R, C);
            }else{
                return null;
            }
        }
        
        private int[][] prop1(int[][] L, int[][] C)
        {
            if(C == null){
//                C = L; // read only
                C = new int[S][];
                for(int i = 0;i < S;i++){
                    C[i] = Arrays.copyOf(L[i], S);
                }
            }else{
                for(int i = 0;i < S;i++){
                    C[i] = Arrays.copyOf(L[i], S);
                }
            }
            return C;
        }
        
        public void update(int pos, long x) {
            int[][] M = {{1, 1}, {1, 0}};
            int[] v = {1, 0};
            v = pow(M, v, x-1);
            node[H+pos][0][2] += v[0];
            if(node[H+pos][0][2] >= mod)node[H+pos][0][2] -= mod;
            node[H+pos][1][2] += v[1];
            if(node[H+pos][1][2] >= mod)node[H+pos][1][2] -= mod;
            node[H+pos][3][2] += v[0];
            if(node[H+pos][3][2] >= mod)node[H+pos][3][2] -= mod;
            for(int i = H+pos>>>1;i >= 1;i>>>=1)propagate(i);
        }
        
        public int[] apply(int l, int r, int[] v){
            return apply(l, r, 0, H, 1, v);
        }
        
        protected int[] apply(int l, int r, int cl, int cr, int cur, int[] v)
        {
            if(l <= cl && cr <= r){
                return mul(node[cur], v, mod);
            }else{
                int mid = cl+cr>>>1;
                if(cl < r && l < mid){
                    v = apply(l, r, cl, mid, 2*cur, v);
                }
                if(mid < r && l < cr){
                    v = apply(l, r, mid, cr, 2*cur+1, v);
                }
                return v;
            }
        }
        
        
        public static int[] mul(int[][] A, int[] v, int mod)
        {
            int m = A.length;
            int n = v.length;
            int[] w = new int[m];
            for(int i = 0;i < m;i++){
                long sum = 0;
                for(int k = 0;k < n;k++){
                    sum += (long)A[i][k] * v[k];
                    if(sum >= BIG)sum -= BIG;
                }
                w[i] = (int)(sum % mod);
            }
            return w;
        }
        
        public static int[][] mul(int[][] A, int[][] B, int[][] C, int mod)
        {
            int m = A.length;
            int n = A[0].length;
            int o = B[0].length;
            if(C == null)C = new int[m][o];
            for(int i = 0;i < m;i++){
                for(int j = 0;j < o;j++){
                    long sum = 0;
                    for(int k = 0;k < n;k++){
                        sum += (long)A[i][k] * B[k][j];
                        if(sum >= BIG)sum -= BIG;
                    }
                    sum %= mod;
                    C[i][j] = (int)sum;
                }
            }
            return C;
        }
        
        // A^e*v
        public static int[] pow(int[][] A, int[] v, long e)
        {
            for(int i = 0;i < v.length;i++){
                if(v[i] >= mod)v[i] %= mod;
            }
            int[][] MUL = A;
            for(;e > 0;e>>>=1) {
                if((e&1)==1)v = mul(MUL, v);
                MUL = p2(MUL);
            }
            return v;
        }
        
        // int matrix*int vector
        public static int[] mul(int[][] A, int[] v)
        {
            int m = A.length;
            int n = v.length;
            int[] w = new int[m];
            for(int i = 0;i < m;i++){
                long sum = 0;
                for(int k = 0;k < n;k++){
                    sum += (long)A[i][k] * v[k];
                    if(sum >= BIG)sum -= BIG;
                }
                w[i] = (int)(sum % mod);
            }
            return w;
        }
        
        // int matrix^2 (be careful about negative value)
        public static int[][] p2(int[][] A)
        {
            int n = A.length;
            int[][] C = new int[n][n];
            for(int i = 0;i < n;i++){
                long[] sum = new long[n];
                for(int k = 0;k < n;k++){
                    for(int j = 0;j < n;j++){
                        sum[j] += (long)A[i][k] * A[k][j];
                        if(sum[j] >= BIG)sum[j] -= BIG;
                    }
                }
                for(int j = 0;j < n;j++){
                    C[i][j] = (int)(sum[j] % mod);
                }
            }
            return C;
        }

    }    
    
    public static int lca2(int a, int b, int[][] spar, int[] depth) {
        if (depth[a] < depth[b]) {
            b = ancestor(b, depth[b] - depth[a], spar);
        } else if (depth[a] > depth[b]) {
            a = ancestor(a, depth[a] - depth[b], spar);
        }

        if (a == b)
            return a;
        int sa = a, sb = b;
        for (int low = 0, high = depth[a], t = Integer.highestOneBit(high), k = Integer
                .numberOfTrailingZeros(t); t > 0; t >>>= 1, k--) {
            if ((low ^ high) >= t) {
                if (spar[k][sa] != spar[k][sb]) {
                    low |= t;
                    sa = spar[k][sa];
                    sb = spar[k][sb];
                } else {
                    high = low | t - 1;
                }
            }
        }
        return spar[0][sa];
    }

    protected static int ancestor(int a, int m, int[][] spar) {
        for (int i = 0; m > 0 && a != -1; m >>>= 1, i++) {
            if ((m & 1) == 1)
                a = spar[i][a];
        }
        return a;
    }

    public static int[][] logstepParents(int[] par) {
        int n = par.length;
        int m = Integer.numberOfTrailingZeros(Integer.highestOneBit(n - 1)) + 1;
        int[][] pars = new int[m][n];
        pars[0] = par;
        for (int j = 1; j < m; j++) {
            for (int i = 0; i < n; i++) {
                pars[j][i] = pars[j - 1][i] == -1 ? -1
                        : pars[j - 1][pars[j - 1][i]];
            }
        }
        return pars;
    }

    
    public static int[] decomposeToHeavyLight(int[][] g, int[] par, int[] ord) {
        int n = g.length;
        int[] size = new int[n];
        Arrays.fill(size, 1);
        for (int i = n - 1; i > 0; i--)
            size[par[ord[i]]] += size[ord[i]];

        int[] clus = new int[n];
        Arrays.fill(clus, -1);
        int p = 0;
        outer: for (int i = 0; i < n; i++) {
            int u = ord[i];
            if (clus[u] == -1)
                clus[u] = p++;
            for (int v : g[u]) {
                if (par[u] != v && size[v] >= size[u] / 2) {
                    clus[v] = clus[u];
                    continue outer;
                }
            }
            for (int v : g[u]) {
                if (par[u] != v) {
                    clus[v] = clus[u];
                    break;
                }
            }
        }
        return clus;
    }

    public static int[][] clusPaths(int[] clus, int[] ord) {
        int n = clus.length;
        int[] rp = new int[n];
        int sup = 0;
        for (int i = 0; i < n; i++) {
            rp[clus[i]]++;
            sup = Math.max(sup, clus[i]);
        }
        sup++;

        int[][] row = new int[sup][];
        for (int i = 0; i < sup; i++)
            row[i] = new int[rp[i]];

        for (int i = n - 1; i >= 0; i--) {
            row[clus[ord[i]]][--rp[clus[ord[i]]]] = ord[i];
        }
        return row;
    }

    public static int[] clusIInd(int[][] clusPath, int n) {
        int[] iind = new int[n];
        for (int[] path : clusPath) {
            for (int i = 0; i < path.length; i++) {
                iind[path[i]] = i;
            }
        }
        return iind;
    }
    
    public static int[][] parentToG(int[] par)
    {
        int n = par.length;
        int[] ct = new int[n];
        for(int i = 0;i < n;i++){
            if(par[i] >= 0){
                ct[i]++;
                ct[par[i]]++;
            }
        }
        int[][] g = new int[n][];
        for(int i = 0;i < n;i++){
            g[i] = new int[ct[i]];
        }
        for(int i = 0;i < n;i++){
            if(par[i] >= 0){
                g[par[i]][--ct[par[i]]] = i;
                g[i][--ct[i]] = par[i];
            }
        }
        return g;
    }


    public static int[][] parents3(int[][] g, int root) {
        int n = g.length;
        int[] par = new int[n];
        Arrays.fill(par, -1);

        int[] depth = new int[n];
        depth[0] = 0;

        int[] q = new int[n];
        q[0] = root;
        for (int p = 0, r = 1; p < r; p++) {
            int cur = q[p];
            for (int nex : g[cur]) {
                if (par[cur] != nex) {
                    q[r++] = nex;
                    par[nex] = cur;
                    depth[nex] = depth[cur] + 1;
                }
            }
        }
        return new int[][] { par, q, depth };
    }

    static int[][] packU(int n, int[] from, int[] to) {
        int[][] g = new int[n][];
        int[] p = new int[n];
        for (int f : from)
            p[f]++;
        for (int t : to)
            p[t]++;
        for (int i = 0; i < n; i++)
            g[i] = new int[p[i]];
        for (int i = 0; i < from.length; i++) {
            g[from[i]][--p[from[i]]] = to[i];
            g[to[i]][--p[to[i]]] = from[i];
        }
        return g;
    }
    
    void run() throws Exception
    {
        is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
        out = new PrintWriter(System.out);
        
        long s = System.currentTimeMillis();
        solve();
        out.flush();
        if(!INPUT.isEmpty())tr(System.currentTimeMillis()-s+"ms");
    }
    
    public static void main(String[] args) throws Exception { new H().run(); }
    
    private byte[] inbuf = new byte[1024];
    private int lenbuf = 0, ptrbuf = 0;
    
    private int readByte()
    {
        if(lenbuf == -1)throw new InputMismatchException();
        if(ptrbuf >= lenbuf){
            ptrbuf = 0;
            try { lenbuf = is.read(inbuf); } catch (IOException e) { throw new InputMismatchException(); }
            if(lenbuf <= 0)return -1;
        }
        return inbuf[ptrbuf++];
    }
    
    private boolean isSpaceChar(int c) { return !(c >= 33 && c <= 126); }
    private int skip() { int b; while((b = readByte()) != -1 && isSpaceChar(b)); return b; }
    
    private double nd() { return Double.parseDouble(ns()); }
    private char nc() { return (char)skip(); }
    
    private String ns()
    {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while(!(isSpaceChar(b))){ // when nextLine, (isSpaceChar(b) && b != ' ')
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    
    private char[] ns(int n)
    {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while(p < n && !(isSpaceChar(b))){
            buf[p++] = (char)b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }
    
    private char[][] nm(int n, int m)
    {
        char[][] map = new char[n][];
        for(int i = 0;i < n;i++)map[i] = ns(m);
        return map;
    }
    
    private int[] na(int n)
    {
        int[] a = new int[n];
        for(int i = 0;i < n;i++)a[i] = ni();
        return a;
    }
    
    private int ni()
    {
        int num = 0, b;
        boolean minus = false;
        while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        
        while(true){
            if(b >= '0' && b <= '9'){
                num = num * 10 + (b - '0');
            }else{
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private long nl()
    {
        long num = 0;
        int b;
        boolean minus = false;
        while((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-'));
        if(b == '-'){
            minus = true;
            b = readByte();
        }
        
        while(true){
            if(b >= '0' && b <= '9'){
                num = num * 10 + (b - '0');
            }else{
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
    
    private static void tr(Object... o) { System.out.println(Arrays.deepToString(o)); }
}