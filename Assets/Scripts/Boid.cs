using UnityEngine;

public class Boid : MonoBehaviour
{
    public float speed = 1f;
    public float LargeRadius = 20f;
    public float SmallRadius = 10f;

    private float speedScale = -0.5f;

    public float STheta = 1f;
    public float SZeta = 1f;
    
    private Vector2 position;
    private Vector2 velocity;
    private Vector3 position3d;

    private void Start()
    {
        position = new Vector2(Random.Range(0f, 2f*Mathf.PI), Random.Range(0f, 2f*Mathf.PI));
        // velocity = new Vector2(Random.Range(-1f, 1f), Random.Range(-1f, 1f));
        velocity = new Vector2(Random.Range(0.5f, 1f), Random.Range(0.5f, 1f));
        velocity.x = speedScale * (velocity.x / velocity.magnitude);
        velocity.y = speedScale * (velocity.y / velocity.magnitude);
    }

    public Vector3 getposition3d
    {
        get { return position3d; }
    }

    private void Update()
    {
        Debug.Log(1.0 / Time.deltaTime);
        position += velocity * speed * Time.deltaTime;
        // position.x = (position.x + 2f*Mathf.PI) % (2f*Mathf.PI);
        // position.y = (position.y + 2f*Mathf.PI) % (2f*Mathf.PI);

        float x = (LargeRadius + (SmallRadius * Mathf.Cos(position.x))) * Mathf.Cos(position.y);
        float y = SZeta * (LargeRadius + (SmallRadius * Mathf.Cos(position.x))) * Mathf.Sin(position.y);
        float z = STheta * SmallRadius * Mathf.Sin(position.x);

        // transform.position = new Vector3(x, y, z);
        transform.position = new Vector3(x, z, y);
        position3d = new Vector3(x, z, y);
    }
}