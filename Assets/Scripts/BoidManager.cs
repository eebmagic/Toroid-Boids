using UnityEngine;

public class BoidManager : MonoBehaviour
{
    public GameObject boidPrefab;
    public int numBoids = 10;
    public float sphereRadius = 1f;

    private Boid[] boids;

    private void Start()
    {
        boids = new Boid[numBoids];

        for (int i = 0; i < numBoids; i++)
        {
            GameObject boidGO = Instantiate(boidPrefab);
            boids[i] = boidGO.AddComponent<Boid>();
        }
    }

    // void OnDrawGizmos()
    // {
    //     Gizmos.color = Color.yellow;
    //     for (int i = 0; i < numBoids; i++)
    //     {
    //         Gizmos.DrawSphere(boids[i].getposition3d, sphereRadius);
    //     }
    // }
}