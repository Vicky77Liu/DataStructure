import java.util.TreeMap;

public class HashTable<K,V>{
    private TreeMap<K,V>[] hashtable;
    private int M;
    private  int size;

    public HashTable(int M){
        this.M = M;
        size = 0;
        hashtable = new TreeMap[M];
        for(int i = 0;i < M; i++)
            hashtable[i] = new TreeMap<>();
    }

    public HashTable(){
        this(97);
    }

    private  int hash(K key){
        return (key.hashCode() & 0x7fffffff) % M;
    }

    public void add(K key, V val){
        TreeMap<K,V> map = hashtable[hash(key)];
        if(map.containsKey(key))
            map.put(key,val);
        else{
            map.put(key,val);
            size ++;
        }
    }
    public V remove(K key){
        TreeMap<K,V> map = hashtable[hash(key)];
        V ret = null;
        if(map.containsKey(key)){
            ret = map.remove(key);
            size --;
        }
        return ret;
    }

    public boolean contains(K key){
        return hashtable[hash(key)].containsKey(key);
    }

    public void set(K key, V val){
        TreeMap<K,V> map = hashtable[hash(key)];
        if(!map.containsKey(key))
            throw new IllealArgumentException(key + "do not exit!");
        map.put(key,val);
    }

    public V get(K key){
        return hashtable[hash(key)].get(key);
    }

}
